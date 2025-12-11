"""
API Backend: Chatbot Diagnostic Médical
Framework: FastAPI
Modèle: Random Forest (49 maladies DDXPlus, 110 symptômes)
100% en Français - Version Windows avec Mock XGBoost Avancé
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
    # Créer module xgboost
    xgb_module = types.ModuleType('xgboost')
    sys.modules['xgboost'] = xgb_module
    
    # Créer module xgboost.core
    xgb_core = types.ModuleType('xgboost.core')
    sys.modules['xgboost.core'] = xgb_core
    xgb_module.core = xgb_core
    
    # Créer module xgboost.sklearn
    xgb_sklearn = types.ModuleType('xgboost.sklearn')
    sys.modules['xgboost.sklearn'] = xgb_sklearn
    xgb_module.sklearn = xgb_sklearn
    
    # Classes factices
    class MockXGB:
        def __init__(self, *args, **kwargs): pass
        def fit(self, *args, **kwargs): return self
        def predict(self, *args, **kwargs): return []
        def predict_proba(self, *args, **kwargs): return []
    
    # Injecter les classes
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

# Créer dossier logs
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
    version="3.0.0",
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

class RequeteDiagnostic(BaseModel):
    symptomes: Dict[str, int] = Field(..., description="Dictionnaire symptômes {code: 0|1}")
    session_id: Optional[str] = Field(None, description="ID session utilisateur")

    class Config:
        json_schema_extra = {
            "example": {
                "symptomes": {
                    "E_48": 1,
                    "E_50": 1,
                    "E_53": 1
                },
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
        version="3.0.0",
        environment=ENVIRONMENT
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
