@"
"""
Traductions COMPLÈTES: Symptômes et Maladies en Français
Dataset DDXPlus: 110 symptômes + 49 maladies
Source: https://github.com/mila-iqia/ddxplus
"""

# ========== TRADUCTIONS SYMPTÔMES (110) ==========
SYMPTOMES_FR = {
    # Symptômes respiratoires
    'E_32': 'Toux grasse',
    'E_33': 'Toux sèche',
    'E_48': 'Fièvre',
    'E_50': 'Toux',
    'E_53': 'Mal de gorge',
    'E_54_@_V_161': 'Congestion nasale',
    'E_54_@_V_179': 'Sinusite',
    'E_54_@_V_181': 'Obstruction nasale',
    'E_54_@_V_192': 'Nez bouché',
    'E_55_@_V_89': 'Nez qui coule',
    'E_56_@_4': 'Éternuements',
    'E_91': 'Essoufflement',
    'E_167': 'Respiration sifflante',
    
    # Symptômes généraux
    'E_57_@_V_123': 'Fatigue',
    'E_58_@_3': 'Frissons',
    'E_59_@_3': 'Sueurs',
    'E_66': 'Fièvre élevée (>39°C)',
    'E_77': 'Mal de tête',
    'E_108': 'Faiblesse générale',
    'E_109': 'Vertiges',
    'E_110': "Perte d'appétit",
    
    # Symptômes digestifs
    'E_87': 'Nausées',
    'E_111': 'Diarrhée',
    'E_201': 'Douleur abdominale',
    'E_222': 'Vomissements',
    
    # Symptômes cardiaques/thoraciques
    'E_79': 'Douleur thoracique',
    'E_97': 'Difficulté à avaler',
    
    # Symptômes musculo-squelettiques
    'E_105': 'Douleur articulaire',
    'E_106': 'Douleur musculaire',
    'E_129': 'Raideur nuque',
    
    # Symptômes neurologiques
    'E_131_@_V_10': 'Sensibilité à la lumière',
    'E_204_@_V_10': 'Écoulement nasal',
}

# ========== TRADUCTIONS MALADIES (49 pathologies DDXPlus) ==========
MALADIES_FR = {
    0: ('Exacerbation BPCO / infection', 'Aggravation de la bronchopneumopathie chronique obstructive'),
    1: ('Réactions dystoniques aiguës', 'Contractions musculaires involontaires dues à médicaments'),
    2: ('Laryngite aiguë', 'Inflammation du larynx'),
    3: ('Otite moyenne aiguë', 'Infection de l oreille moyenne'),
    4: ('Œdème pulmonaire aigu', 'Accumulation de liquide dans les poumons'),
    5: ('Rhinosinusite aiguë', 'Inflammation aiguë des sinus nasaux'),
    6: ('Sinusite allergique', 'Inflammation des sinus due aux allergies'),
    7: ('Choc anaphylactique', 'Réaction allergique sévère mettant la vie en danger'),
    8: ('Anémie', 'Manque de globules rouges ou hémoglobine'),
    9: ('Fibrillation auriculaire', 'Rythme cardiaque irrégulier et rapide'),
    10: ('Vertige positionnel bénin', 'Vertiges lors des changements de position'),
    11: ('Colique biliaire', 'Douleur due aux calculs biliaires'),
    12: ('Syndrome de Boerhaave', 'Rupture de l œsophage'),
    13: ('Bronchospasme / Exacerbation asthme aigu', 'Rétrécissement soudain des voies respiratoires'),
    14: ('Bronchite aiguë', 'Inflammation des bronches'),
    15: ('Bronchiolite', 'Infection virale des petites voies respiratoires'),
    16: ('Bronchiectasie', 'Dilatation anormale des bronches'),
    17: ('Cholécystite', 'Inflammation de la vésicule biliaire'),
    18: ('Maladie de Chagas', 'Infection parasitaire tropicale'),
    19: ('Sinusite chronique', 'Inflammation chronique des sinus'),
    20: ('Pneumonie communautaire', 'Infection pulmonaire acquise hors hôpital'),
    21: ('Céphalée en grappe', 'Maux de tête sévères unilatéraux'),
    22: ('Laryngotrachéite (Croup)', 'Infection virale des voies respiratoires supérieures'),
    23: ('Ebola', 'Maladie virale hémorragique'),
    24: ('Épiglottite', 'Inflammation de l épiglotte'),
    25: ('RGO (Reflux gastro-œsophagien)', 'Remontées acides de l estomac'),
    26: ('Syndrome de Guillain-Barré', 'Maladie auto-immune affectant les nerfs'),
    27: ('VIH (infection initiale)', 'Infection par le virus de l immunodéficience humaine'),
    28: ('Grippe (Influenza)', 'Infection virale respiratoire saisonnière'),
    29: ('Hernie inguinale', 'Saillie d organes à travers la paroi abdominale'),
    30: ('Laryngospasme', 'Contraction soudaine du larynx'),
    31: ('Œdème localisé', 'Gonflement localisé dû à accumulation de liquide'),
    32: ('Migraine', 'Mal de tête intense avec nausées'),
    33: ('Myasthénie grave', 'Faiblesse musculaire auto-immune'),
    34: ('Myocardite', 'Inflammation du muscle cardiaque'),
    35: ('Néoplasme pancréatique', 'Tumeur du pancréas'),
    36: ('Attaque de panique', 'Épisode soudain de peur intense'),
    37: ('Péricardite', 'Inflammation de l enveloppe du cœur'),
    38: ('Pneumothorax spontané', 'Affaissement spontané du poumon'),
    39: ('Infarctus possible (NSTEMI/STEMI)', 'Crise cardiaque'),
    40: ('TSVP (Tachycardie supraventriculaire)', 'Rythme cardiaque très rapide'),
    41: ('Embolie pulmonaire', 'Obstruction artérielle pulmonaire par caillot'),
    42: ('Néoplasme pulmonaire', 'Tumeur du poumon'),
    43: ('Sarcoïdose', 'Maladie inflammatoire multi-organes'),
    44: ('Intoxication alimentaire (Scombroid)', 'Empoisonnement par histamine du poisson'),
    45: ('Lupus érythémateux disséminé (LED)', 'Maladie auto-immune systémique'),
    46: ('Angine stable', 'Douleur thoracique stable à l effort'),
    47: ('Tuberculose', 'Infection bactérienne pulmonaire'),
    48: ('Angine instable', 'Douleur thoracique imprévisible au repos'),
}

# Note: Le dataset original a 49 pathologies, pas 51
# Source: DDXPlus NeurIPS 2022 dataset

def get_symptome_fr(code):
    """Obtenir traduction symptôme en français"""
    return SYMPTOMES_FR.get(code, code)

def get_maladie_fr(indice):
    """Obtenir nom maladie en français"""
    if indice in MALADIES_FR:
        return MALADIES_FR[indice][0]
    return f"Maladie {indice}"

def get_description_maladie(indice):
    """Obtenir description maladie en français"""
    if indice in MALADIES_FR:
        return MALADIES_FR[indice][1]
    return ""

# Liste complète pour export
def get_all_symptomes():
    """Retourner tous les symptômes"""
    return list(SYMPTOMES_FR.items())

def get_all_maladies():
    """Retourner toutes les maladies"""
    return list(MALADIES_FR.items())
"@ | Out-File -FilePath traductions.py -Encoding UTF8

Write-Host "✅ traductions.py créé avec 49 maladies DDXPlus" -ForegroundColor Green

# Vérifier nombre de lignes
(Get-Content traductions.py).Count
