"""
Traductions COMPLÈTES: Symptômes et Maladies en Français
Basé sur l'analyse complète du notebook chatbotnlp.ipynb (181 codes uniques)
"""

# ========== TRADUCTIONS SYMPTÔMES & ANTÉCÉDENTS ==========
SYMPTOMES_FR = {
    # --- SYMPTÔMES GÉNÉRAUX ---
    'E_48': 'Fièvre',
    'E_66': 'Fièvre élevée (>39°C)',
    'E_57_@_V_123': 'Fatigue intense / Malaise',
    'E_58_@_3': 'Frissons',
    'E_59_@_3': 'Sueurs nocturnes',
    'E_110': "Perte d'appétit",
    'E_108': 'Faiblesse générale',
    'E_109': 'Vertiges / Étourdissements',
    'E_200': 'Perte de poids involontaire',
    'E_125': 'Gain de poids involontaire',
    'E_98': 'Palpitations cardiaques',
    'E_101': 'Perte de connaissance (Syncope)',
    'E_215': 'Pâleur',
    'E_148': 'Confusion mentale',
    'E_149': 'Désorientation',
    'E_41': 'Mauvaise haleine',
    'E_45': 'Bouche sèche',

    # --- DOULEURS (LOCALISATION) ---
    'E_77': 'Mal de tête',
    'E_78': 'Mal de tête pulsatile',
    'E_79': 'Douleur thoracique',
    'E_80': 'Douleur thoracique (serrement)',
    'E_81': 'Douleur thoracique (poignard)',
    'E_82': 'Douleur thoracique (brûlure)',
    'E_201': 'Douleur abdominale',
    'E_154': 'Douleur estomac (Haut centre)',
    'E_155': 'Douleur foie (Haut droite)',
    'E_156': 'Douleur fosse iliaque droite (Bas droite)',
    'E_157': 'Douleur flanc droit',
    'E_158': 'Douleur flanc gauche',
    'E_159': 'Douleur fosse iliaque gauche (Bas gauche)',
    'E_160': 'Douleur bas ventre (Hypogastre)',
    'E_162': 'Douleur reins (Flancs)',
    'E_144': 'Douleur lombaire (Bas du dos)',
    'E_105': 'Douleurs articulaires',
    'E_106': 'Douleurs musculaires',
    'E_129': 'Raideur de la nuque',
    'E_130': 'Douleur cervicale',
    'E_130_@_V_156': 'Douleur cervicale irradiante',
    'E_134': 'Douleur épaule',
    'E_135': 'Douleur bras',
    'E_136': 'Douleur jambe',
    'E_188': 'Douleur oreille',
    'E_168': 'Douleur œil',
    'E_219': 'Douleur à la respiration',

    # --- RESPIRATOIRE & ORL ---
    'E_50': 'Toux',
    'E_50_@_V_161': 'Toux (contexte viral)',
    'E_32': 'Toux grasse (productive)',
    'E_33': 'Toux sèche',
    'E_51': 'Crachats / Glaires',
    'E_52': 'Crachats de sang',
    'E_91': 'Essoufflement (Dyspnée)',
    'E_167': 'Respiration sifflante',
    'E_181': 'Respiration rapide',
    'E_53': 'Mal de gorge',
    'E_49': 'Voix enrouée',
    
    # NEZ & SINUS (Complets)
    'E_54_@_V_161': 'Nez bouché',
    'E_54_@_V_179': 'Douleur aux sinus',
    'E_54_@_V_154': 'Congestion nasale sévère',
    'E_54_@_V_180': 'Nez bouché (matin)',
    'E_54_@_V_181': 'Nez bouché (soir)',
    'E_54_@_V_182': 'Obstruction nasale unilatérale',
    'E_54_@_V_183': 'Obstruction nasale bilatérale',
    'E_54_@_V_192': 'Sensation de nez plein',
    'E_54_@_V_198': 'Nez bouché chronique',
    
    # ÉCOULEMENT NASAL (Toutes les variantes E_55)
    'E_55_@_V_89': 'Nez qui coule (clair)',
    'E_55_@_V_165': 'Nez qui coule (purulent)',
    'E_55_@_V_56': 'Nez qui coule (Rhinorrhée)',
    'E_55_@_V_55': 'Nez qui coule abondamment',
    'E_55_@_V_62': 'Goutte au nez',
    'E_55_@_V_101': 'Écoulement nasal postérieur',
    'E_55_@_V_104': 'Nez qui coule (allergie)',
    'E_55_@_V_108': 'Nez qui coule (infection)',
    'E_55_@_V_109': 'Sécrétions nasales épaisses',
    'E_55_@_V_124': 'Mucus nasal',
    'E_55_@_V_137': 'Nez humide',
    'E_55_@_V_148': 'Rhinorrhée antérieure',
    'E_55_@_V_159': 'Rhinorrhée postérieure',
    'E_55_@_V_160': 'Écoulement nasal jaune',
    'E_55_@_V_163': 'Écoulement nasal vert',
    'E_55_@_V_166': 'Écoulement nasal sanglant',
    'E_55_@_V_167': 'Croûtes dans le nez',
    'E_55_@_V_170': 'Sécheresse nasale', # Paradoxal mais présent dans le groupe E55 parfois
    'E_55_@_V_171': 'Démangeaison nasale',
    'E_55_@_V_187': 'Éternuements fréquents (rhinite)',
    'E_55_@_V_197': 'Reniflements',
    'E_55_@_V_20': 'Nez qui coule (hiver)',
    'E_55_@_V_21': 'Nez qui coule (printemps)',
    'E_55_@_V_25': 'Nez qui coule (animaux)',
    'E_55_@_V_29': 'Nez qui coule (poussière)',
    'E_55_@_V_33': 'Nez qui coule (matin)',

    # ÉTERNUEMENTS (Variantes E_56)
    'E_56_@_2': 'Éternuements (salves)',
    'E_56_@_3': 'Éternuements matinaux',
    'E_56_@_4': 'Éternuements',
    'E_56_@_5': 'Éternuements (poussière)',
    'E_56_@_6': 'Éternuements (animaux)',
    'E_56_@_7': 'Éternuements (pollen)',
    'E_56_@_8': 'Éternuements (froid)',

    'E_204_@_V_10': 'Écoulement dans l\'arrière-gorge',
    'E_204_@_V_11': 'Glaire dans la gorge',
    'E_171': 'Ganglions enflés (Cou)',

    # --- DIGESTIF ---
    'E_87': 'Nausées',
    'E_88': 'Vomissements',
    'E_89': 'Vomissements de sang',
    'E_111': 'Diarrhée',
    'E_112': 'Constipation',
    'E_92': 'Brûlures d\'estomac / Reflux',
    'E_97': 'Difficulté à avaler (Dysphagie)',
    'E_222': 'Vomissements alimentaires',
    'E_115': 'Selles noires (Méléna)',
    'E_116': 'Sang rouge dans les selles',
    'E_113': 'Gaz / Ballonnements',
    
    # --- PEAU, YEUX & DIVERS ---
    'E_183': 'Éruption cutanée (Boutons/Rougeurs)',
    'E_184': 'Démangeaisons',
    'E_185': 'Rougeur cutanée localisée',
    'E_216': 'Lèvres ou doigts bleutés',
    'E_131_@_V_10': 'Yeux sensibles à la lumière',
    'E_169': 'Rougeur de l\'œil',
    'E_170': 'Yeux qui pleurent',
    'E_205': 'Paupières gonflées',
    'E_206': 'Chevilles / Pieds gonflés',
    'E_220': 'Fourmillements / Engourdissements',
    'E_221': 'Perte de sensibilité',
    
    # --- PSYCHOLOGIE ---
    'E_151': 'Anxiété / Angoisse',
    'E_225': 'Sentiment de dépression',
    'E_224': 'Insomnie / Troubles du sommeil',
    'E_36': 'Attaque de panique',
    
    # --- MANQUANTS DU NOTEBOOK (104 à 227) ---
    'E_104': 'Douleur articulaire (général)',
    'E_114': 'Incontinence fécale',
    'E_117': 'Hémorroïdes',
    'E_118': 'Douleur anale',
    'E_119': 'Prurit anal',
    'E_120': 'Masse abdominale',
    'E_121': 'Distension abdominale',
    'E_122': 'Ascite',
    'E_123': 'Ictère (Jaunisse)',
    'E_124': 'Urines foncées',
    'E_126': 'Polyphagie (Faim excessive)',
    'E_127': 'Polydipsie (Soif excessive)',
    'E_128': 'Polyurie (Urine fréquente)',
    'E_132': 'Douleur machoire',
    'E_132_@_0': 'Trismus',
    'E_133': 'Douleur épaule',
    'E_134_@_0': 'Raideur épaule',
    'E_135_@_V_10': 'Faiblesse bras',
    'E_135_@_V_12': 'Engourdissement bras',
    'E_136_@_0': 'Faiblesse jambe',
    'E_137': 'Crampes musculaires',
    'E_138': 'Tremblements',
    'E_139': 'Ataxie (Trouble coordination)',
    'E_140': 'Paralysie faciale',
    'E_141': 'Trouble de la parole',
    'E_142': 'Trouble de la vision',
    'E_143': 'Diplopie (Vision double)',
    'E_145': 'Sciatique',
    'E_146': 'Lumbago',
    'E_147': 'Trouble de la conscience',
    'E_150': 'Agitation',
    'E_152': 'Hallucinations',
    'E_153': 'Idées suicidaires',
    'E_161': 'Douleur testiculaire',
    'E_163': 'Douleur pelvienne',
    'E_164': 'Pertes vaginales',
    'E_165': 'Saignement vaginal anormal',
    'E_166': 'Dysménorrhée',
    'E_172': 'Goitre',
    'E_173': 'Nodule thyroïdien',
    'E_174': 'Œdème articulaire',
    'E_175': 'Raideur articulaire',
    'E_176': 'Déformation articulaire',
    'E_177': 'Crepitus',
    'E_178': 'Instabilité articulaire',
    'E_179': 'Blocage articulaire',
    'E_180': 'Boiterie',
    'E_182': 'Cyanose',
    'E_186': 'Ecchymoses faciles',
    'E_208': 'Sueurs froides',
    'E_209': 'Mains moites',
    'E_214': 'Teint gris',
    'E_217': 'Marbrures',
    'E_218': 'Peau froide',
    'E_226': 'Asthénie',
    'E_227': 'Anorexie',
    
    # --- FRISSONS & FATIGUE (Variantes) ---
    'E_57_@_V_30': 'Fatigue matinale',
    'E_57_@_V_31': 'Fatigue vesperale',
    'E_57_@_V_39': 'Fatigue chronique',
    'E_58_@_2': 'Frissons (fièvre)',
    'E_58_@_4': 'Frissons solennels',
    'E_58_@_5': 'Frissons (froid)',
    'E_58_@_6': 'Chair de poule',
    'E_58_@_7': 'Tremblements de froid',
    'E_58_@_8': 'Sensation de froid interne',
    
    # --- SUEURS (Variantes) ---
    'E_59_@_0': 'Transpiration excessive',
    'E_59_@_1': 'Sueurs chaudes',
    'E_59_@_2': 'Sueurs froides',
    'E_59_@_4': 'Sueurs profuses',
    'E_59_@_5': 'Sueurs généralisées',
    'E_59_@_6': 'Sueurs localisées',
    
    # --- AUTRES ---
    'E_69': 'Fièvre modérée',
    'E_70': 'Fébricule',
    'E_76': 'Céphalée tension',
}

# ========== TRADUCTIONS MALADIES (49 pathologies DDXPlus) ==========
MALADIES_FR = {
    0: ('Exacerbation BPCO', 'Aggravation de la maladie pulmonaire chronique'),
    1: ('Réactions dystoniques', 'Contractions musculaires involontaires (médicament)'),
    2: ('Laryngite aiguë', 'Inflammation de la gorge/larynx'),
    3: ('Otite moyenne', 'Infection de l oreille'),
    4: ('Œdème pulmonaire', 'Eau dans les poumons (Urgence)'),
    5: ('Rhinosinusite aiguë', 'Infection des sinus'),
    6: ('Sinusite allergique', 'Allergie nasale'),
    7: ('Choc anaphylactique', 'Réaction allergique grave (Urgence)'),
    8: ('Anémie', 'Manque de fer/globules rouges'),
    9: ('Fibrillation auriculaire', 'Trouble du rythme cardiaque'),
    10: ('Vertige positionnel', 'Vertiges aux mouvements de tête'),
    11: ('Colique biliaire', 'Calculs dans la vésicule'),
    12: ('Syndrome de Boerhaave', 'Rupture œsophage (Urgence)'),
    13: ('Crise d\'asthme', 'Difficulté respiratoire asthmatique'),
    14: ('Bronchite aiguë', 'Bronchite virale ou bactérienne'),
    15: ('Bronchiolite', 'Infection respiratoire (souvent infantile)'),
    16: ('Bronchiectasie', 'Dilatation des bronches'),
    17: ('Cholécystite', 'Infection de la vésicule biliaire'),
    18: ('Maladie de Chagas', 'Infection parasitaire'),
    19: ('Sinusite chronique', 'Sinusite persistante'),
    20: ('Pneumonie', 'Infection pulmonaire'),
    21: ('Céphalée en grappe', 'Maux de tête intenses par crises'),
    22: ('Croup', 'Laryngite de l\'enfant'),
    23: ('Ebola', 'Fièvre hémorragique virale'),
    24: ('Épiglottite', 'Infection de la gorge (Urgence)'),
    25: ('Reflux RGO', 'Remontées acides'),
    26: ('Guillain-Barré', 'Paralysie progressive (Urgence)'),
    27: ('Primo-infection VIH', 'Infection virale récente'),
    28: ('Grippe', 'Virus Influenza'),
    29: ('Hernie inguinale', 'Hernie de l\'aine'),
    30: ('Laryngospasme', 'Blocage de la respiration'),
    31: ('Œdème localisé', 'Gonflement local'),
    32: ('Migraine', 'Maux de tête forts'),
    33: ('Myasthénie', 'Faiblesse musculaire chronique'),
    34: ('Myocardite', 'Inflammation du cœur'),
    35: ('Cancer pancréas', 'Tumeur pancréatique'),
    36: ('Attaque de panique', 'Crise d\'angoisse'),
    37: ('Péricardite', 'Inflammation enveloppe du cœur'),
    38: ('Pneumothorax', 'Décollement de la plèvre (Urgence)'),
    39: ('Infarctus (Crise cardiaque)', 'Arrêt sanguin au cœur (Urgence)'),
    40: ('Tachycardie', 'Cœur qui bat trop vite'),
    41: ('Embolie pulmonaire', 'Caillot dans le poumon (Urgence)'),
    42: ('Cancer du poumon', 'Tumeur pulmonaire'),
    43: ('Sarcoïdose', 'Maladie inflammatoire'),
    44: ('Intoxication poisson', 'Intoxication alimentaire'),
    45: ('Lupus', 'Maladie auto-immune'),
    46: ('Angine de poitrine stable', 'Douleur cardiaque à l\'effort'),
    47: ('Tuberculose', 'Infection pulmonaire grave'),
    48: ('Angine instable', 'Douleur cardiaque au repos (Urgence)'),
}

def get_symptome_fr(code):
    """
    Obtenir traduction symptôme en français
    INTELLIGENT FALLBACK: Nettoie les codes inconnus pour les rendre lisibles
    """
    if code in SYMPTOMES_FR:
        return SYMPTOMES_FR[code]
    
    # Fallback pour les codes V_ (Antécédents) non explicités
    if code.startswith("V_"):
        return f"Antécédent (Code {code.replace('V_', '')})"

    # Nettoyage générique
    clean = code.replace("E_", "").replace("V_", "")
    if "_@_" in code:
        parts = clean.split("_@_")
        if len(parts) == 2:
            return f"Symptôme {parts[0]} (Type {parts[1]})"
    
    return f"Symptôme {clean.replace('_', ' ')}"

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
