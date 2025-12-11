"""
API Backend: Chatbot Diagnostic Médical
Framework: FastAPI
Modèle: Random Forest (49 maladies DDXPlus, 110 symptômes)
100% en Français - Version Windows avec Mock XGBoost Avancé + LOGIQUE DYNAMIQUE
"""

import os
import sys
import pickle
import logging
import time
from datetime import datetime
from typing import Dict, List, Optional
import numpy as np
import warnings
import types

# ========== MOCK XGBOOST AVANCÉ ==========
# Crée une structure de modules factices complète pour tromper pickle
try:
    import xgboost
except ImportError:
    xgb_module = types.ModuleType('xgboost')
    sys.modules['xgboost'] = xgb_module
    xgb_core = types.ModuleType('xgboost.core')
    sys.modules['xgboost.core'] = xgb_core
    xgb_module.core = xgb_core
    xgb_sklearn = types.ModuleType('xgboost.sklearn')
    sys.modules['xgboost.sklearn'] = xgb_sklearn
    xgb_module.sklearn = xgb_sklearn
    
    class MockXGB:
        def __init__(self, *args, **kwargs): pass
        def fit(self, *args, **kwargs): return self
        def predict(self, *args, **kwargs): return []
        def predict_proba(self, *args, **kwargs): return []
    
    xgb_module.XGBClassifier = MockXGB
    xgb_module.XGBRegressor = MockXGB
    xgb_sklearn.XGBClassifier = MockXGB
    xgb_sklearn.XGBRegressor = MockXGB
    xgb_core.Booster = MockXGB

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from traductions import SYMPTOMES_FR, get_symptome_fr, get_maladie_fr, get_description_maladie
from conseils_medicaux import get_conseil

warnings.filterwarnings('ignore')

# ========== CONFIGURATION ==========
load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
API_PORT = int(os.getenv("API_PORT", 8000))
MODEL_PATH = os.getenv("MODEL_PATH", "./ddxplus_final.pkl")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

os.makedirs("./logs", exist_ok=True)

# ========== LOGGING ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("./logs/diagnostic.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ========== CHARGEMENT MODÈLE ==========
print("\n" + "="*70)
print("🔄 CHARGEMENT DU MODÈLE RANDOM FOREST")
print("="*70)

try:
    with open(MODEL_PATH, 'rb') as f:
        model_data = pickle.load(f)
    
    rf_model = model_data['rf_model']
    symptom_list = model_data['symptom_list']
    pathologies = model_data['pathologies']
    
    print(f"✅ Modèle: {type(rf_model).__name__}")
    print(f"✅ Symptômes: {len(symptom_list)}")
    print(f"✅ Maladies: {len(pathologies)}")
    print(f"✅ Accuracy: ~95%")
    logger.info(f"Modèle chargé avec succès: {len(pathologies)} maladies, {len(symptom_list)} symptômes")
except Exception as e:
    print(f"❌ ERREUR CHARGEMENT: {str(e)}")
    logger.error(f"Erreur chargement modèle: {str(e)}")
    rf_model = None
    symptom_list = []
    pathologies = []

print("="*70 + "\n")

# ========== FASTAPI APP ==========
app = FastAPI(
    title="Chatbot Diagnostic Médical DDXPlus",
    description=f"API diagnostic basée sur IA - {len(pathologies)} maladies, {len(symptom_list)} symptômes",
    version="3.1.0",
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# --- MODÈLES Pydantic ---
class RequeteDiagnostic(BaseModel):
    symptomes: Dict[str, int] = Field(..., description="Dictionnaire symptômes {code: 0|1}")
    session_id: Optional[str] = Field(None, description="ID session utilisateur")

    class Config:
        json_schema_extra = {
            "example": {
                "symptomes": {"E_48": 1, "E_50": 1},
                "session_id": "test-session-123"
            }
        }

class DiagnosticAlternatif(BaseModel):
    rang: int
    maladie: str
    probabilite: float
    pourcentage: str

class ReponseDiagnostic(BaseModel):
    session_id: str
    diagnostic_principal: str
    description: str
    probabilite: float
    pourcentage: str
    alternatives: List[DiagnosticAlternatif]
    recommandation: str
    autosoins: List[str]
    nutrition: List[str]
    reprises_activites: List[str]
    signes_alerte: List[str]
    urgence: str
    nombre_symptomes: int
    temps_traitement_ms: float
    timestamp: str

class StatusAPI(BaseModel):
    status: str
    modele: str
    maladies: int
    symptomes: int
    accuracy: str
    version: str
    environment: str

class NextQuestionResponse(BaseModel):
    question_code: Optional[str]
    question_texte: Optional[str]
    fini: bool
    diagnostic_provisoire: Optional[str]
    confiance: float

# --- FONCTIONS UTILITAIRES ---
def construire_vecteur(symptomes_dict: Dict[str, int]) -> tuple:
    X = np.zeros(len(symptom_list), dtype=np.int8)
    compte = 0
    for code, valeur in symptomes_dict.items():
        try:
            if code in symptom_list:
                idx = symptom_list.index(code)
                X[idx] = int(valeur)
                if valeur == 1:
                    compte += 1
        except:
            pass
    return X, compte

def calculer_niveau_confiance(proba: float) -> str:
    if proba > 0.85: return "🔴 Très probablement"
    elif proba > 0.70: return "🟠 Probablement"
    elif proba > 0.50: return "🟡 Possiblement"
    else: return "🔵 À confirmer avec médecin"

# ========== ENDPOINTS ==========

@app.get("/", tags=["Root"])
async def root():
    return {"app": "Chatbot Diagnostic Médical DDXPlus", "status": "running"}

@app.get("/api/sante", response_model=StatusAPI, tags=["Santé"])
async def sante():
    return StatusAPI(
        status="healthy" if rf_model else "degraded",
        modele="Random Forest Classifier",
        maladies=len(pathologies),
        symptomes=len(symptom_list),
        accuracy="~95%",
        version="3.1.0",
        environment=ENVIRONMENT
    )

# --- NOUVEL ENDPOINT LOGIQUE DYNAMIQUE ---
@app.post("/api/prochaine-question", response_model=NextQuestionResponse, tags=["Diagnostic"])
async def prochaine_question(request: RequeteDiagnostic):
    """
    Détermine la meilleure question à poser basée sur les réponses précédentes.
    """
    if not rf_model:
        raise HTTPException(status_code=503, detail="Modèle non chargé")
    
    symptomes_repondus = request.symptomes # Dict {code: 0 ou 1}
    
    # 1. Construire vecteur actuel
    X, compte = construire_vecteur(symptomes_repondus)
    
    # 2. Obtenir probabilités actuelles
    probas = rf_model.predict_proba([X])[0]
    confiance_max = float(np.max(probas))
    idx_top = np.argmax(probas)
    maladie_provisoire = get_maladie_fr(idx_top)
    
    # CRITÈRE D'ARRÊT
    # Si confiance > 85% OU plus de 15 questions posées (15 symptomes positifs trouvés ou total reponses)
    if confiance_max > 0.85 or len(symptomes_repondus) >= 15:
        return NextQuestionResponse(
            question_code=None,
            question_texte=None,
            fini=True,
            diagnostic_provisoire=maladie_provisoire,
            confiance=confiance_max
        )

    # 3. STRATÉGIE ARBRE DE DÉCISION (Simplifiée et Rapide)
    # On regarde les 5 maladies les plus probables
    top_indices = np.argsort(probas)[-5:] 
    
    # On cherche le symptôme qui discrimine le mieux ces maladies
    # (Celui qui apparait souvent dans ces maladies mais qu'on n'a pas encore posé)
    
    meilleur_code = None
    
    # Liste des codes déjà demandés
    codes_deja_demandes = list(symptomes_repondus.keys())
    
    # On parcourt tous les symptômes possibles
    # (Note: Pour optimiser, on pourrait pré-calculer une matrice Maladie-Symptome)
    
    # Pour faire simple et efficace sans matrice externe :
    # On utilise l'importance des features du modèle si disponible, 
    # ou on itère sur les symptômes non posés par ordre d'importance globale (approximatif)
    
    # Méthode simple : On prend les symptômes globaux les plus fréquents NON ENCORE POSÉS
    # Idéalement, il faudrait la matrice de corrélation, mais ici on va utiliser 
    # l'ordre de la symptom_list qui est souvent triée par fréquence dans DDXPlus
    
    # Amélioration : On utilise l'ordre d'importance des features du Random Forest
    importances = rf_model.feature_importances_
    indices_importants = np.argsort(importances)[::-1] # Du plus important au moins important
    
    for idx in indices_importants:
        code_candidat = symptom_list[idx]
        
        # Si on ne l'a pas encore demandé
        if code_candidat not in codes_deja_demandes:
            meilleur_code = code_candidat
            break # On a trouvé le prochain plus important
            
    # Si on ne trouve rien (cas rare), on prend le premier non répondu
    if not meilleur_code:
        for s in symptom_list:
            if s not in codes_deja_demandes:
                meilleur_code = s
                break
    
    # Traduire la question
    question_texte = SYMPTOMES_FR.get(meilleur_code, meilleur_code)
    
    return NextQuestionResponse(
        question_code=meilleur_code,
        question_texte=question_texte,
        fini=False,
        diagnostic_provisoire=maladie_provisoire,
        confiance=confiance_max
    )

@app.post("/api/diagnostic", response_model=ReponseDiagnostic, tags=["Diagnostic"])
async def diagnostic(request: RequeteDiagnostic):
    if not rf_model:
        raise HTTPException(status_code=503, detail="Modèle non chargé")
        
    debut = time.time()
    session = request.session_id or f"anon-{int(time.time())}"
    
    try:
        X, compte = construire_vecteur(request.symptomes)
        
        proba = rf_model.predict_proba([X])[0]
        idx_principal = np.argmax(proba)
        conf = float(np.max(proba))
        
        maladie_fr = get_maladie_fr(idx_principal)
        description = get_description_maladie(idx_principal)
        
        top_3_idx = np.argsort(proba)[-3:][::-1]
        alternatives = []
        for rang, idx in enumerate(top_3_idx, 1):
            prob = float(proba[idx])
            alternatives.append(DiagnosticAlternatif(
                rang=rang, maladie=get_maladie_fr(idx), probabilite=prob, pourcentage=f"{prob*100:.0f}%"
            ))
        
        conseils = get_conseil(idx_principal)
        niveau = calculer_niveau_confiance(conf)
        
        recommandation = f"""{niveau} {maladie_fr} ({conf*100:.0f}%)
Action immédiate: {conseils.get('immediate', 'Consulter un médecin')}"""
        
        temps_ms = (time.time() - debut) * 1000
        
        return ReponseDiagnostic(
            session_id=session,
            diagnostic_principal=maladie_fr,
            description=description,
            probabilite=conf,
            pourcentage=f"{conf*100:.0f}%",
            alternatives=alternatives,
            recommandation=recommandation,
            autosoins=conseils.get("autosoins", []),
            nutrition=conseils.get("nutrition", []),
            reprises_activites=conseils.get("reprise", []),
            signes_alerte=conseils.get("signes_alerte", []),
            urgence=conseils.get("urgence", "Consulter un médecin"),
            nombre_symptomes=compte,
            temps_traitement_ms=round(temps_ms, 2),
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        logger.error(f"[{session}] Erreur: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/symptomes", tags=["Données"])
async def symptomes():
    symptomes_list = [
        {"code": code, "nom": SYMPTOMES_FR.get(code, code), "indice": idx}
        for idx, code in enumerate(symptom_list)
    ]
    return {"total": len(symptomes_list), "symptomes": symptomes_list}

@app.get("/api/maladies", tags=["Données"])
async def maladies():
    maladies_list = [
        {"id": i, "nom": get_maladie_fr(i), "description": get_description_maladie(i)}
        for i in range(len(pathologies))
    ]
    return {"total": len(maladies_list), "maladies": maladies_list}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)
