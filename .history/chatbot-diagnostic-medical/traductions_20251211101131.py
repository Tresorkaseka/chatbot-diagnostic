"""
Traductions COMPLÈTES: Symptômes et Maladies en Français
Dataset DDXPlus: ~110 symptômes/antécédents + 49 maladies
"""

# ========== TRADUCTIONS SYMPTÔMES & ANTÉCÉDENTS ==========
SYMPTOMES_FR = {
    # GÉNÉRAUX
    'E_48': 'Fièvre',
    'E_66': 'Fièvre élevée (>39°C)',
    'E_57_@_V_123': 'Fatigue intense',
    'E_58_@_3': 'Frissons',
    'E_59_@_3': 'Sueurs nocturnes',
    'E_110': "Perte d'appétit",
    'E_108': 'Faiblesse générale',
    'E_109': 'Vertiges',
    'E_200': 'Perte de poids involontaire',
    'E_125': 'Gain de poids involontaire',
    'E_98': 'Palpitations',
    'E_101': 'Perte de connaissance (syncope)',
    
    # RESPIRATOIRE
    'E_50': 'Toux',
    'E_32': 'Toux grasse',
    'E_33': 'Toux sèche',
    'E_51': 'Toux avec glaires',
    'E_52': 'Toux avec sang (hémoptysie)',
    'E_91': 'Essoufflement (dyspnée)',
    'E_167': 'Respiration sifflante',
    'E_181': 'Respiration rapide',
    'E_219': 'Douleur à la respiration',
    'E_49': 'Enrouement',
    
    # ORL (Nez, Gorge, Oreilles)
    'E_53': 'Mal de gorge',
    'E_54_@_V_161': 'Congestion nasale',
    'E_54_@_V_179': 'Douleur sinus',
    'E_55_@_V_89': 'Nez qui coule',
    'E_56_@_4': 'Éternuements',
    'E_204_@_V_10': 'Écoulement dans la gorge',
    'E_188': 'Douleur oreille',
    'E_189': 'Baisse audition',
    'E_190': 'Bourdonnements (acouphènes)',
    'E_171': 'Gonflement ganglions cou',
    
    # DIGESTIF
    'E_201': 'Douleur abdominale',
    'E_154': 'Douleur estomac (épigastre)',
    'E_155': 'Douleur foie (hypocondre droit)',
    'E_156': 'Douleur fosse iliaque droite',
    'E_159': 'Douleur fosse iliaque gauche',
    'E_87': 'Nausées',
    'E_88': 'Vomissements',
    'E_89': 'Vomissements sanglants',
    'E_111': 'Diarrhée',
    'E_112': 'Constipation',
    'E_92': 'Brûlures estomac',
    'E_97': 'Difficulté à avaler',
    'E_222': 'Vomissements alimentaires',
    'E_115': 'Sang dans les selles (noir)',
    'E_116': 'Sang dans les selles (rouge)',
    'E_113': 'Gaz excessifs',
    
    # DOULEURS SPÉCIFIQUES
    'E_77': 'Mal de tête',
    'E_78': 'Mal de tête pulsatile',
    'E_79': 'Douleur thoracique',
    'E_80': 'Douleur thoracique (serrement)',
    'E_81': 'Douleur thoracique (poignard)',
    'E_105': 'Douleur articulaire',
    'E_106': 'Douleur musculaire',
    'E_129': 'Raideur nuque',
    'E_162': 'Douleur flanc (rein)',
    'E_144': 'Douleur lombaire',
    'E_130': 'Douleur cervicale',
    'E_134': 'Douleur épaule',
    'E_135': 'Douleur bras',
    'E_136': 'Douleur jambe',
    
    # PEAU & YEUX
    'E_183': 'Éruption cutanée',
    'E_184': 'Démangeaisons',
    'E_185': 'Rougeur cutanée',
    'E_215': 'Pâleur',
    'E_216': 'Lèvres bleues (cyanose)',
    'E_131_@_V_10': 'Sensibilité lumière',
    'E_168': 'Douleur œil',
    'E_169': 'Rougeur œil',
    'E_170': 'Larmoyement',
    'E_205': 'Œdème paupière',
    'E_206': 'Œdème cheville',
    
    # NEURO & PSY
    'E_148': 'Confusion',
    'E_149': 'Désorientation',
    'E_151': 'Anxiété',
    'E_220': 'Fourmillements',
    'E_221': 'Perte sensibilité',
    'E_223': 'Troubles mémoire',
    'E_224': 'Troubles sommeil',
    'E_225': 'Tristesse / Dépression',
    
    # ANTÉCÉDENTS & FACTEURS RISQUE
    'V_11': 'Hypertension',
    'V_12': 'Diabète',
    'V_13': 'Fumeur',
    'V_14': 'Cholestérol',
    'V_22': 'Asthme',
    'V_23': 'Allergies',
    'V_83': 'BPCO',
    'V_122': 'Immunodépression',
    'V_161': 'Contact malade récent',
    'V_18': 'Grossesse',
    'V_19': 'Antécédents cardiaques',
    'V_20': 'Cancer',
    'V_21': 'VIH/SIDA',
    'V_24': 'Alcoolisme',
    'V_25': 'Drogues IV',
    'V_26': 'Voyage récent',
    'V_27': 'Chirurgie récente',
    'V_28': 'Immobilisation prolongée'
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

def get_all_symptomes():
    """Retourner tous les symptômes"""
    return list(SYMPTOMES_FR.items())

def get_all_maladies():
    """Retourner toutes les maladies"""
    return list(MALADIES_FR.items())
