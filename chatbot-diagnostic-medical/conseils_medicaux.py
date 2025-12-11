"""
Conseils médicaux COMPLETS pour les 49 maladies DDXPlus
100% en Français - Version Windows compatible
"""

CONSEILS = {
    0: {  # Exacerbation BPCO
        'urgence': '⚠️ URGENCE si difficultés respiratoires',
        'immediate': 'Bronchodilatateurs prescrits immédiatement',
        'autosoins': ['✓ Bronchodilatateurs (salbutamol)', '✓ Corticostéroïdes si prescrits', '✓ Position assise verticale', '✓ Oxygène si SpO2 < 90%'],
        'nutrition': ['Hydratation 2L/jour', 'Aliments légers', 'Éviter irritants'],
        'reprise': ['Repos strict 5-7 jours', 'Suivi pneumologue', 'Monitoring oxymétrie'],
        'signes_alerte': ['🚨 Respiration > 30/min', '🚨 SpO2 < 90%', '🚨 Confusion', '🚨 Cyanose']
    },
    1: {  # Réactions dystoniques
        'urgence': '⚠️ URGENCE - Contractions involontaires',
        'immediate': 'Antihistaminiques (diphenhydramine) immédiatement',
        'autosoins': ['✓ Diphenhydramine 50mg IM/IV', '✓ Anticholinergiques si prescrits', '✓ Éviter alcool', '✓ Repos environnement calme'],
        'nutrition': ['Hydratation si possible', 'Aliments liquides', 'Éviter caféine'],
        'reprise': ['Immobilisation jusqu à résolution', 'Surveillance 24h', 'Ajustement médicaments'],
        'signes_alerte': ['🚨 Laryngospasme', '🚨 Difficultés respiratoires', '🚨 Rigidité', '🚨 Hyperthermie']
    },
    2: {  # Laryngite
        'urgence': 'Consulter si respiration difficile',
        'immediate': 'Repos vocal complet 3-7 jours',
        'autosoins': ['✓ Silence vocal strict', '✓ Hydratation 2-3L/jour tiède', '✓ Paracétamol si douleur', '✓ Humidificateur'],
        'nutrition': ['Eau tiède miel', 'Tisanes', 'Soupes tièdes', 'Éviter épices'],
        'reprise': ['Inhalations vapeur 3x/jour', 'Gargarismes eau salée', 'Éviter efforts vocaux 7-10j'],
        'signes_alerte': ['🚨 Stridor repos', '🚨 Dyspnée sévère', '🚨 Fièvre > 40°C', '🚨 Incapacité avaler']
    },
    3: {  # Otite moyenne
        'urgence': 'Consulter si douleur intense',
        'immediate': 'Antalgiques + chaleur locale',
        'autosoins': ['✓ Paracétamol/ibuprofène', '✓ Compresse chaude 15min', '✓ Position semi-assise', '✓ Antibiotiques si prescrits'],
        'nutrition': ['Hydratation abondante', 'Aliments mous', 'Éviter laitiers si congestion'],
        'reprise': ['Antibiotiques 7-10j complet', 'Repos 3-5j', 'Suivi ORL si récidive'],
        'signes_alerte': ['🚨 Écoulement purulent', '🚨 Fièvre > 39°C', '🚨 Vertige', '🚨 Surdité brutale']
    },
    4: {  # Œdème pulmonaire
        'urgence': '🚨 URGENCE VITALE - 15/112 immédiatement',
        'immediate': 'Position assise jambes pendantes + oxygène',
        'autosoins': ['✓ Position assise stricte', '✓ Diurétiques IV (furosémide)', '✓ Oxygène 100%', '✓ Morphine si prescrite'],
        'nutrition': ['Restriction hydrique stricte', 'Régime sans sel', 'Rien par voie orale'],
        'reprise': ['Hospitalisation obligatoire', 'Monitoring cardiaque', 'Bilan cardiologique'],
        'signes_alerte': ['🚨 Mousse rosée', '🚨 SpO2 < 85%', '🚨 Sueurs profuses', '🚨 Agitation']
    },
    5: {  # Rhinosinusite aiguë
        'urgence': 'Consulter si > 10 jours',
        'immediate': 'Lavages nasaux + antalgiques',
        'autosoins': ['✓ Lavages nasaux 4-6x/jour', '✓ Paracétamol 1g/6h', '✓ Inhalations vapeur', '✓ Décongestionnants max 3j'],
        'nutrition': ['Hydratation 2-3L/jour', 'Bouillons chauds', 'Épices douces', 'Éviter laitiers'],
        'reprise': ['Repos 5-7j', 'Éviter climatisation', 'Humidifier air'],
        'signes_alerte': ['🚨 Fièvre > 39°C > 3j', '🚨 Œdème facial', '🚨 Troubles visuels', '🚨 Céphalées intenses']
    },
    6: {  # Sinusite allergique
        'urgence': 'Généralement pas urgence',
        'immediate': 'Antihistaminiques + lavages nasaux',
        'autosoins': ['✓ Antihistaminiques (cétirizine)', '✓ Lavages nasaux réguliers', '✓ Éviter allergènes', '✓ Corticoïdes nasaux'],
        'nutrition': ['Hydratation régulière', 'Éviter aliments histaminiques', 'Alimentation anti-inflammatoire'],
        'reprise': ['Identifier allergènes', 'Traitement désensibilisation possible', 'Suivi allergologue'],
        'signes_alerte': ['🚨 Asthme associé', '🚨 Œdème facial', '🚨 Fièvre élevée']
    },
    7: {  # Choc anaphylactique
        'urgence': '🚨🚨 URGENCE ABSOLUE - 15/112',
        'immediate': 'Adrénaline auto-injecteur IMMÉDIATEMENT',
        'autosoins': ['✓ Adrénaline 0.3mg IM cuisse', '✓ Position allongée jambes surélevées', '✓ 2e dose si pas amélioration 5-15min', '✓ Oxygène haute concentration'],
        'nutrition': ['Rien par voie orale', 'Éviter allergène identifié à vie'],
        'reprise': ['Hospitalisation surveillance 24h', 'Prescription adrénaline auto-injecteur', 'Bilan allergologique'],
        'signes_alerte': ['🚨 Urticaire généralisée', '🚨 Œdème Quincke', '🚨 Bronchospasme', '🚨 Choc']
    },
    8: {  # Anémie
        'urgence': 'Consulter si symptômes sévères',
        'immediate': 'Supplémentation fer + repos',
        'autosoins': ['✓ Fer 100-200mg/jour', '✓ Vitamine C pour absorption', '✓ Repos augmenté', '✓ Éviter efforts intenses'],
        'nutrition': ['Viandes rouges', 'Légumes verts', 'Fruits secs', 'Vitamine C'],
        'reprise': ['Bilan étiologique obligatoire', 'Suivi hématologique', 'Transfusion si Hb < 7g/dL'],
        'signes_alerte': ['🚨 Fatigue extrême', '🚨 Palpitations repos', '🚨 Dyspnée effort minime', '🚨 Syncope']
    },
    9: {  # Fibrillation auriculaire
        'urgence': 'Consulter rapidement si 1er épisode',
        'immediate': 'Contrôle fréquence + anticoagulation',
        'autosoins': ['✓ Bêtabloquants si prescrits', '✓ Anticoagulants (warfarine/AOD)', '✓ Éviter caféine alcool', '✓ Repos'],
        'nutrition': ['Régime pauvre sel', 'Éviter caféine', 'Limiter alcool', 'Surveillance INR si AVK'],
        'reprise': ['Cardioversion si indiquée', 'Anticoagulation long terme', 'Suivi cardiologique régulier'],
        'signes_alerte': ['🚨 Douleur thoracique', '🚨 Dyspnée', '🚨 Syncope', '🚨 AVC signes']
    },
    10: {  # Vertige positionnel
        'urgence': 'Généralement bénin',
        'immediate': 'Manœuvres repositionnement (Epley)',
        'autosoins': ['✓ Manœuvre Epley par professionnel', '✓ Éviter mouvements brusques', '✓ Antivertigineux si prescrits', '✓ Rééducation vestibulaire'],
        'nutrition': ['Hydratation régulière', 'Éviter alcool', 'Limiter sel'],
        'reprise': ['Exercices Brandt-Daroff', 'Éviter positions déclenchantes', 'Amélioration spontanée souvent'],
        'signes_alerte': ['🚨 Surdité', '🚨 Acouphènes', '🚨 Céphalées', '🚨 Troubles neurologiques']
    },
    11: {  # Colique biliaire
        'urgence': 'Consulter si douleur persistante',
        'immediate': 'Antalgiques + antispasmodiques',
        'autosoins': ['✓ Paracétamol 1g', '✓ Antispasmodiques (phloroglucinol)', '✓ Jeûne temporaire', '✓ Chaleur locale'],
        'nutrition': ['Régime pauvre graisses', 'Petits repas fréquents', 'Éviter œufs chocolat'],
        'reprise': ['Échographie biliaire', 'Cholécystectomie si récidive', 'Régime adapté'],
        'signes_alerte': ['🚨 Fièvre', '🚨 Ictère', '🚨 Vomissements persistants', '🚨 Douleur > 6h']
    },
    12: {  # Syndrome de Boerhaave
        'urgence': '🚨 URGENCE CHIRURGICALE - 15/112',
        'immediate': 'Hospitalisation chirurgie thoracique immédiate',
        'autosoins': ['✓ Position semi-assise', '✓ Jeûne absolu', '✓ Analgésie IV', '✓ Antibiotiques large spectre IV'],
        'nutrition': ['Jeûne absolu', 'Nutrition parentérale', 'Alimentation après chirurgie'],
        'reprise': ['Chirurgie urgente obligatoire', 'Soins intensifs', 'Pronostic grave'],
        'signes_alerte': ['🚨 Douleur thoracique post-vomissements', '🚨 Emphysème sous-cutané', '🚨 Choc', '🚨 Dyspnée']
    },
    13: {  # Bronchospasme / Asthme
        'urgence': '⚠️ URGENCE si crise sévère',
        'immediate': 'Bronchodilatateurs inhalés répétés',
        'autosoins': ['✓ Salbutamol 4-10 bouffées', '✓ Position assise', '✓ Corticoïdes PO/IV si sévère', '✓ Oxygène si SpO2 < 92%'],
        'nutrition': ['Hydratation', 'Éviter allergènes alimentaires', 'Alimentation anti-inflammatoire'],
        'reprise': ['Traitement fond contrôle', 'Plan action asthme', 'Éviter déclencheurs'],
        'signes_alerte': ['🚨 Impossibilité parler', '🚨 SpO2 < 90%', '🚨 Tirage', '🚨 Silence auscultatoire']
    },
    14: {  # Bronchite aiguë
        'urgence': 'Généralement pas urgence',
        'immediate': 'Repos + hydratation + antitussifs',
        'autosoins': ['✓ Repos 7-10j', '✓ Hydratation 2-3L/jour', '✓ Antitussifs si toux sèche', '✓ Expectorants si grasse'],
        'nutrition': ['Liquides chauds', 'Miel citron', 'Éviter laitiers', 'Vitamine C'],
        'reprise': ['Généralement virale', 'Antibiotiques rarement nécessaires', 'Amélioration 2-3 semaines'],
        'signes_alerte': ['🚨 Fièvre > 38.5°C > 5j', '🚨 Dyspnée', '🚨 Hémoptysie', '🚨 Douleur thoracique']
    },
    15: {  # Bronchiolite
        'urgence': 'Urgence si nourrisson < 6 mois',
        'immediate': 'Désobstruction nasale + surveillance',
        'autosoins': ['✓ DRP nasale sérum phy avant repas', '✓ Fractionnement repas', '✓ Couchage incliné 30°', '✓ Hydratation'],
        'nutrition': ['Petits repas fréquents', 'Hydratation fractionnée', 'Lait maternel privilégié'],
        'reprise': ['Kinésithérapie respiratoire', 'Surveillance SpO2', 'Hospitalisation si critères'],
        'signes_alerte': ['🚨 SpO2 < 92%', '🚨 Refus alimentation', '🚨 Apnées', '🚨 Détresse respiratoire']
    },
    16: {  # Bronchiectasie
        'urgence': 'Consulter si exacerbation',
        'immediate': 'Drainage bronchique + antibiotiques',
        'autosoins': ['✓ Kinésithérapie respiratoire quotidienne', '✓ Drainage postural', '✓ Mucolytiques', '✓ Antibiotiques si surinfection'],
        'nutrition': ['Hydratation optimale', 'Alimentation équilibrée', 'Suppléments si dénutrition'],
        'reprise': ['Suivi pneumologique régulier', 'Vaccination grippe/pneumocoque', 'Éviter tabac'],
        'signes_alerte': ['🚨 Hémoptysie', '🚨 Fièvre', '🚨 Expectoration purulente', '🚨 Dyspnée aggravée']
    },
    17: {  # Cholécystite
        'urgence': 'Consulter rapidement',
        'immediate': 'Antibiotiques + antalgiques + jeûne',
        'autosoins': ['✓ Jeûne strict', '✓ Antibiotiques IV', '✓ Antalgiques morphiniques', '✓ Hydratation IV'],
        'nutrition': ['Jeûne 48-72h', 'Réalimentation progressive pauvre graisses', 'Éviter aliments déclenchants'],
        'reprise': ['Cholécystectomie sous 72h recommandée', 'Hospitalisation', 'Surveillance complications'],
        'signes_alerte': ['🚨 Fièvre > 38.5°C', '🚨 Défense abdominale', '🚨 Ictère', '🚨 Sepsis']
    },
    18: {  # Maladie de Chagas
        'urgence': 'Consulter spécialiste maladies tropicales',
        'immediate': 'Traitement antiparasitaire (benznidazole)',
        'autosoins': ['✓ Benznidazole 5-7mg/kg/j 60j', '✓ Nifurtimox alternative', '✓ Suivi cardiologique', '✓ Éviter vecteurs'],
        'nutrition': ['Alimentation équilibrée', 'Hydratation', 'Suppléments si cardiopathie'],
        'reprise': ['Traitement phase aiguë efficace', 'Surveillance cardiaque long terme', 'Prévention transmission'],
        'signes_alerte': ['🚨 Troubles conduction', '🚨 Insuffisance cardiaque', '🚨 Méga-organes', '🚨 Fièvre']
    },
    19: {  # Sinusite chronique
        'urgence': 'Généralement pas urgence',
        'immediate': 'Lavages nasaux + corticoïdes',
        'autosoins': ['✓ Lavages nasaux quotidiens', '✓ Corticoïdes nasaux', '✓ Antibiotiques si surinfection', '✓ Éviter irritants'],
        'nutrition': ['Hydratation', 'Éviter allergènes', 'Anti-inflammatoires naturels'],
        'reprise': ['Bilan allergologique', 'Scanner sinus si échec', 'Chirurgie si indications'],
        'signes_alerte': ['🚨 Exacerbations fréquentes', '🚨 Complications orbitaires', '🚨 Céphalées sévères']
    },
    20: {  # Pneumonie communautaire
        'urgence': 'Consulter rapidement',
        'immediate': 'Antibiotiques + repos + hydratation',
        'autosoins': ['✓ Antibiotiques selon antibiogramme', '✓ Repos strict', '✓ Hydratation 2-3L/jour', '✓ Antalgiques antipyrétiques'],
        'nutrition': ['Hydratation abondante', 'Alimentation légère', 'Protéines', 'Vitamine C'],
        'reprise': ['Antibiotiques 7-14j', 'Hospitalisation si critères sévérité', 'Radiographie contrôle 6 semaines'],
        'signes_alerte': ['🚨 SpO2 < 92%', '🚨 Fréquence resp > 30/min', '🚨 Confusion', '🚨 Hypotension']
    },
    21: {  # Céphalée en grappe
        'urgence': 'Traitement abortif rapide nécessaire',
        'immediate': 'Oxygène 100% + sumatriptan',
        'autosoins': ['✓ Oxygène 12-15L/min 15-20min', '✓ Sumatriptan 6mg SC', '✓ Éviter alcool', '✓ Traitement prophylactique'],
        'nutrition': ['Éviter alcool période grappes', 'Éviter déclencheurs', 'Régularité repas'],
        'reprise': ['Vérapamil prophylaxie', 'Éviter siestes', 'Suivi neurologique'],
        'signes_alerte': ['🚨 Changement pattern', '🚨 Signes neurologiques', '🚨 Résistance traitement']
    },
    22: {  # Laryngotrachéite (Croup)
        'urgence': 'Urgence si stridor repos',
        'immediate': 'Corticoïdes + humidification',
        'autosoins': ['✓ Dexaméthasone 0.6mg/kg PO', '✓ Humidificateur vapeur froide', '✓ Adrénaline nébulisée si sévère', '✓ Position assise'],
        'nutrition': ['Liquides froids', 'Hydratation fractionnée', 'Éviter irritants'],
        'reprise': ['Amélioration 2-5j', 'Surveillance stridor', 'Hospitalisation si critères'],
        'signes_alerte': ['🚨 Stridor repos', '🚨 Tirage', '🚨 Cyanose', '🚨 Agitation']
    },
    23: {  # Ebola
        'urgence': '🚨🚨 URGENCE SANITAIRE - Isolement strict',
        'immediate': 'Isolement + soins support + déclaration',
        'autosoins': ['✓ Isolement haute sécurité', '✓ Réhydratation IV massive', '✓ Soins symptomatiques', '✓ Antiviraux expérimentaux'],
        'nutrition': ['Nutrition parentérale', 'Hydratation IV', 'Électrolytes'],
        'reprise': ['Mortalité 25-90%', 'Soins intensifs', 'Déclaration obligatoire', 'Enquête épidémiologique'],
        'signes_alerte': ['🚨 Hémorragies', '🚨 Choc', '🚨 Défaillance multi-organes', '🚨 Fièvre > 38.3°C']
    },
    24: {  # Épiglottite
        'urgence': '🚨 URGENCE VITALE - Ne pas allonger',
        'immediate': 'Position assise + oxygène + antibiotiques IV',
        'autosoins': ['✓ Position assise stricte', '✓ Oxygène humidifié', '✓ Ceftriaxone IV', '✓ Intubation si détresse'],
        'nutrition': ['Jeûne absolu initial', 'Réalimentation après sécurisation'],
        'reprise': ['Hospitalisation USI', 'Intubation préventive parfois', 'Antibiotiques 7-10j'],
        'signes_alerte': ['🚨 Hypersalivation', '🚨 Position tripode', '🚨 Stridor', '🚨 Dysphagie totale']
    },
    25: {  # RGO
        'urgence': 'Généralement pas urgence',
        'immediate': 'IPP + mesures hygiéno-diététiques',
        'autosoins': ['✓ Inhibiteurs pompe protons', '✓ Surélévation tête lit 15cm', '✓ Éviter repas copieux soir', '✓ Arrêt tabac'],
        'nutrition': ['Éviter graisses épices chocolat', 'Petits repas', 'Éviter alcool café', 'Dernière prise 3h avant coucher'],
        'reprise': ['IPP 4-8 semaines', 'Endoscopie si alarme', 'Chirurgie si échec médical'],
        'signes_alerte': ['🚨 Dysphagie', '🚨 Amaigrissement', '🚨 Hémorragie', '🚨 Anémie']
    },
    26: {  # Syndrome Guillain-Barré
        'urgence': '🚨 URGENCE NEUROLOGIQUE',
        'immediate': 'Hospitalisation USI + immunothérapie',
        'autosoins': ['✓ Immunoglobulines IV 0.4g/kg/j 5j', '✓ Plasmaphérèse alternative', '✓ Surveillance respiratoire', '✓ Prophylaxie thromboembolique'],
        'nutrition': ['Nutrition adaptée dysphagie', 'Sonde si nécessaire', 'Hydratation'],
        'reprise': ['Hospitalisation prolongée', 'Rééducation intensive', 'Récupération progressive mois-années'],
        'signes_alerte': ['🚨 Paralysie ascendante', '🚨 Détresse respiratoire', '🚨 Dysautonomie', '🚨 Troubles déglutition']
    },
    27: {  # VIH infection initiale
        'urgence': 'Consulter rapidement pour traitement',
        'immediate': 'Antirétroviraux trithérapie immédiate',
        'autosoins': ['✓ Trithérapie ARV à vie', '✓ Observance stricte', '✓ Suivi charge virale CD4', '✓ Prévention infections opportunistes'],
        'nutrition': ['Alimentation équilibrée', 'Suppléments si besoin', 'Hygiène alimentaire stricte'],
        'reprise': ['Traitement à vie', 'Charge virale indétectable = non transmissible', 'Espérance vie normale si traité'],
        'signes_alerte': ['🚨 Infections opportunistes', '🚨 CD4 < 200', '🚨 Charge virale élevée', '🚨 Effets secondaires ARV']
    },
    28: {  # Grippe
        'urgence': 'Consulter si groupes risque',
        'immediate': 'Repos + antiviraux si < 48h',
        'autosoins': ['✓ Repos complet 7-10j', '✓ Paracétamol 1g/6h', '✓ Oseltamivir si < 48h', '✓ Hydratation 2-3L/jour'],
        'nutrition': ['Bouillons', 'Fruits vitamine C', 'Miel citron', 'Éviter alcool'],
        'reprise': ['Isolement 5-7j', 'Reprise progressive', 'Vaccination annuelle'],
        'signes_alerte': ['🚨 Dyspnée', '🚨 Douleur thoracique', '🚨 Confusion', '🚨 Fièvre > 40°C']
    },
    29: {  # Hernie inguinale
        'urgence': 'URGENCE si étranglement',
        'immediate': 'Chirurgie si symptomatique',
        'autosoins': ['✓ Éviter efforts', '✓ Bandage herniaire temporaire', '✓ Réduction manuelle si réductible', '✓ Consultation chirurgicale'],
        'nutrition': ['Éviter constipation', 'Fibres', 'Hydratation', 'Poids santé'],
        'reprise': ['Chirurgie élective recommandée', 'Récupération 2-4 semaines', 'Éviter efforts 6 semaines'],
        'signes_alerte': ['🚨 Hernie irréductible', '🚨 Douleur intense', '🚨 Vomissements', '🚨 Fièvre']
    },
    30: {  # Laryngospasme
        'urgence': '⚠️ URGENCE si prolongé',
        'immediate': 'Rassurer + position assise + oxygène',
        'autosoins': ['✓ Position assise', '✓ Respiration lente contrôlée', '✓ Oxygène si disponible', '✓ Pression cricothyroïde si sévère'],
        'nutrition': ['Éviter déclencheurs (RGO)', 'Traitement cause sous-jacente'],
        'reprise': ['Investigation cause', 'Traitement RGO si présent', 'Éviter irritants'],
        'signes_alerte': ['🚨 Cyanose', '🚨 Perte conscience', '🚨 Spasme prolongé > 1min']
    },
    31: {  # Œdème localisé
        'urgence': 'Dépend de la cause',
        'immediate': 'Surélévation + compression + investigation',
        'autosoins': ['✓ Surélévation membre', '✓ Compression élastique', '✓ Mobilisation douce', '✓ Diurétiques si prescrits'],
        'nutrition': ['Réduction sel', 'Hydratation modérée', 'Protéines si lymphœdème'],
        'reprise': ['Investigation étiologique', 'Drainage lymphatique si indiqué', 'Traitement cause'],
        'signes_alerte': ['🚨 Douleur intense', '🚨 Chaleur rougeur', '🚨 Extension rapide', '🚨 Dyspnée']
    },
    32: {  # Migraine
        'urgence': 'Consulter si céphalée inhabituelle',
        'immediate': 'Triptans + repos obscurité',
        'autosoins': ['✓ Sumatriptan dès début', '✓ Paracétamol 1g + aspirine 500mg', '✓ Repos obscurité silence', '✓ Compresse froide front'],
        'nutrition': ['Éviter déclencheurs', 'Hydratation régulière', 'Repas réguliers', 'Limiter caféine'],
        'reprise': ['Journal migraines', 'Prophylaxie si > 4/mois', 'Gestion stress'],
        'signes_alerte': ['🚨 Céphalée inhabituelle', '🚨 Déficit neurologique', '🚨 Fièvre', '🚨 Raideur nuque']
    },
    33: {  # Myasthénie grave
        'urgence': 'URGENCE si crise myasthénique',
        'immediate': 'Anticholinestérasiques + immunosuppresseurs',
        'autosoins': ['✓ Pyridostigmine doses régulières', '✓ Corticoïdes', '✓ Éviter médicaments aggravants', '✓ Repos périodes fatigue'],
        'nutrition': ['Aliments faciles à mâcher', 'Repas fractionnés', 'Éviter aliments durs'],
        'reprise': ['Traitement à vie', 'Thymectomie si thymome', 'Surveillance respiratoire'],
        'signes_alerte': ['🚨 Crise myasthénique', '🚨 Détresse respiratoire', '🚨 Dysphagie sévère', '🚨 Ptosis bilatéral']
    },
    34: {  # Myocardite
        'urgence': 'Consulter rapidement',
        'immediate': 'Repos strict + surveillance cardiaque',
        'autosoins': ['✓ Repos strict complet', '✓ Traitement symptomatique IC', '✓ AINS contre-indiqués', '✓ Surveillance ECG troponines'],
        'nutrition': ['Régime sans sel', 'Restriction hydrique si IC', 'Éviter alcool'],
        'reprise': ['Hospitalisation si sévère', 'Arrêt sport 6 mois', 'IRM cardiaque suivi'],
        'signes_alerte': ['🚨 Douleur thoracique', '🚨 Dyspnée', '🚨 Palpitations', '🚨 Syncope']
    },
    35: {  # Néoplasme pancréatique
        'urgence': 'Consultation oncologique rapide',
        'immediate': 'Bilan extension + chirurgie si résécable',
        'autosoins': ['✓ Gestion douleur (morphiniques)', '✓ Enzymes pancréatiques', '✓ Nutrition adaptée', '✓ Support psychologique'],
        'nutrition': ['Repas petits fréquents', 'Enzymes digestives', 'Suppléments', 'Éviter graisses'],
        'reprise': ['Chirurgie (Whipple) si possible', 'Chimiothérapie adjuvante', 'Pronostic réservé'],
        'signes_alerte': ['🚨 Ictère', '🚨 Amaigrissement', '🚨 Douleur dorsale', '🚨 Diabète récent']
    },
    36: {  # Attaque de panique
        'urgence': 'Généralement pas urgence vitale',
        'immediate': 'Rassurer + respiration contrôlée',
        'autosoins': ['✓ Respiration abdominale lente', '✓ Techniques relaxation', '✓ Benzodiazépines si prescrits', '✓ Éviter hyperventilation'],
        'nutrition': ['Éviter caféine', 'Alimentation équilibrée', 'Limiter alcool'],
        'reprise': ['Psychothérapie (TCC)', 'Antidépresseurs si récurrent', 'Gestion stress'],
        'signes_alerte': ['🚨 1ère crise', '🚨 Signes cardiaques atypiques', '🚨 Récurrence fréquente']
    },
    37: {  # Péricardite
        'urgence': 'Consulter rapidement',
        'immediate': 'AINS + colchicine + repos',
        'autosoins': ['✓ Ibuprofène 600mg 3x/j', '✓ Colchicine 0.5mg 2x/j', '✓ Repos strict', '✓ Position assise antalgique'],
        'nutrition': ['Alimentation légère', 'Hydratation', 'Éviter alcool'],
        'reprise': ['Traitement 2-4 semaines', 'Arrêt sport 3 mois', 'Surveillance tamponnade'],
        'signes_alerte': ['🚨 Tamponnade signes', '🚨 Fièvre persistante', '🚨 Dyspnée', '🚨 Hypotension']
    },
    38: {  # Pneumothorax spontané
        'urgence': '⚠️ URGENCE si complet ou sous tension',
        'immediate': 'Exsufflation à l aiguille ou drainage',
        'autosoins': ['✓ Position demi-assise', '✓ Oxygène', '✓ Drainage pleural si > 20%', '✓ Repos strict'],
        'nutrition': ['Alimentation normale', 'Hydratation', 'Éviter efforts Valsalva'],
        'reprise': ['Surveillance radiologique', 'Pleurodèse si récidive', 'Éviter plongée vol 6 semaines'],
        'signes_alerte': ['🚨 Dyspnée sévère', '🚨 Hypotension', '🚨 Emphysème sous-cutané', '🚨 Cyanose']
    },
    39: {  # Infarctus myocarde
        'urgence': '🚨🚨 URGENCE ABSOLUE - 15/112',
        'immediate': 'Aspirine 300mg mâcher + position demi-assise',
        'autosoins': ['✓ Aspirine 300mg MÂCHER', '✓ Position demi-assise', '✓ Trinitrine sublinguale', '✓ NE PAS conduire'],
        'nutrition': ['Rien par VO jusqu à PEC', 'Régime post-IDM sans sel faible graisse'],
        'reprise': ['USI obligatoire', 'Coronarographie urgente', 'Réadaptation 3 mois'],
        'signes_alerte': ['🚨 Douleur > 20min', '🚨 Irradiation', '🚨 Sueurs', '🚨 Malaise']
    },
    40: {  # TSVP (Tachycardie supraventriculaire)
        'urgence': 'Consulter si 1er épisode',
        'immediate': 'Manœuvres vagales + adénosine IV',
        'autosoins': ['✓ Manœuvre Valsalva', '✓ Massage sinus carotidien', '✓ Immersion visage eau froide', '✓ Adénosine 6mg IV si échec'],
        'nutrition': ['Éviter caféine', 'Limiter alcool', 'Hydratation régulière'],
        'reprise': ['Ablation si récurrent', 'Bêtabloquants prophylaxie', 'Suivi cardiologique'],
        'signes_alerte': ['🚨 Syncope', '🚨 Douleur thoracique', '🚨 Hypotension', '🚨 IC signes']
    },
    41: {  # Embolie pulmonaire
        'urgence': '🚨 URGENCE VITALE - 15/112',
        'immediate': 'Oxygène + anticoagulation + hospitalisation',
        'autosoins': ['✓ Position demi-assise', '✓ Oxygène haute concentration', '✓ HBPM SC/IV', '✓ Thrombolyse si massive'],
        'nutrition': ['Restriction hydrique initiale', 'Alimentation post-stabilisation', 'Surveillance INR'],
        'reprise': ['Hospitalisation 5-10j', 'Anticoagulation 3-6 mois', 'Prévention récidive'],
        'signes_alerte': ['🚨 Dyspnée brutale', '🚨 Douleur thoracique', '🚨 Tachycardie', '🚨 Hémoptysie']
    },
    42: {  # Néoplasme pulmonaire
        'urgence': 'Consultation oncologique rapide',
        'immediate': 'Bilan extension + traitement selon stade',
        'autosoins': ['✓ Gestion symptômes', '✓ Oxygène si hypoxie', '✓ Antalgiques', '✓ Support nutritionnel'],
        'nutrition': ['Alimentation enrichie', 'Suppléments protéiques', 'Hydratation'],
        'reprise': ['Chirurgie si résécable', 'Chimiothérapie/radiothérapie', 'Immunothérapie selon type'],
        'signes_alerte': ['🚨 Hémoptysie', '🚨 Syndrome cave sup', '🚨 Détresse respiratoire', '🚨 Amaigrissement']
    },
    43: {  # Sarcoïdose
        'urgence': 'Généralement pas urgence',
        'immediate': 'Corticoïdes si symptomatique',
        'autosoins': ['✓ Prednisone si indiqué', '✓ Surveillance multi-organes', '✓ Vitamine D', '✓ Éviter soleil'],
        'nutrition': ['Régime pauvre calcium', 'Éviter vitamine D excessive', 'Alimentation équilibrée'],
        'reprise': ['Suivi pneumologique régulier', 'Scanner thorax périodique', 'Rémission spontanée possible'],
        'signes_alerte': ['🚨 Atteinte cardiaque', '🚨 Hypercalcémie', '🚨 Uvéite', '🚨 Atteinte neurologique']
    },
    44: {  # Intoxication Scombroid
        'urgence': 'Généralement bénin',
        'immediate': 'Antihistaminiques + arrêt poisson',
        'autosoins': ['✓ Antihistaminiques (cétirizine)', '✓ Corticoïdes si sévère', '✓ Hydratation', '✓ Surveillance réaction'],
        'nutrition': ['Éviter poisson incriminé', 'Hydratation', 'Alimentation légère'],
        'reprise': ['Amélioration 8-12h', 'Éviter poissons mal conservés', 'Généralement bénin'],
        'signes_alerte': ['🚨 Anaphylaxie', '🚨 Bronchospasme', '🚨 Hypotension', '🚨 Œdème Quincke']
    },
    45: {  # Lupus
        'urgence': 'Consulter si poussée',
        'immediate': 'Immunosuppresseurs + protection solaire',
        'autosoins': ['✓ Corticoïdes selon activité', '✓ Hydroxychloroquine', '✓ Protection solaire totale', '✓ Éviter infections'],
        'nutrition': ['Anti-inflammatoire', 'Vitamine D', 'Oméga-3', 'Éviter luzerne'],
        'reprise': ['Suivi rhumatologique régulier', 'Surveillance rénale', 'Traitement vie entière'],
        'signes_alerte': ['🚨 Atteinte rénale', '🚨 Atteinte SNC', '🚨 Poussée sévère', '🚨 Infections']
    },
    46: {  # Angine stable
        'urgence': 'Consulter si modification pattern',
        'immediate': 'Trinitrine + repos + coronarographie',
        'autosoins': ['✓ Trinitrine sublinguale si douleur', '✓ Bêtabloquants', '✓ Antiagrégants', '✓ Statines'],
        'nutrition': ['Régime méditerranéen', 'Réduction graisses saturées', 'Oméga-3', 'Limiter sel'],
        'reprise': ['Revascularisation si indiquée', 'Réadaptation cardiaque', 'Contrôle facteurs risque'],
        'signes_alerte': ['🚨 Douleur repos', '🚨 Augmentation fréquence', '🚨 Durée prolongée', '🚨 Résistance trinitrine']
    },
    47: {  # Tuberculose
        'urgence': 'Déclaration obligatoire + isolement',
        'immediate': 'Quadrithérapie antituberculeuse',
        'autosoins': ['✓ Rifampicine + Isoniazide + Pyrazinamide + Ethambutol', '✓ Traitement 6 mois minimum', '✓ Isolement respiratoire', '✓ Observance stricte'],
        'nutrition': ['Alimentation enrichie', 'Protéines', 'Suppléments vitamine B6', 'Correction dénutrition'],
        'reprise': ['Traitement complet 6-9 mois', 'Surveillance hépatique', 'Non contagieux après 2 semaines traitement'],
        'signes_alerte': ['🚨 Hémoptysie', '🚨 Détresse respiratoire', '🚨 Amaigrissement sévère', '🚨 Résistance']
    },
    48: {  # Angine instable
        'urgence': '🚨 URGENCE CARDIOLOGIQUE - Hospitalisation',
        'immediate': 'Aspirine + HBPM + hospitalisation USI',
        'autosoins': ['✓ Aspirine 300mg', '✓ HBPM anticoagulation', '✓ Repos strict', '✓ Coronarographie urgente programmée'],
        'nutrition': ['Jeûne initial', 'Régime post-coronarien', 'Sans sel faible graisse'],
        'reprise': ['Hospitalisation obligatoire', 'Coronarographie < 72h', 'Revascularisation si indiquée'],
        'signes_alerte': ['🚨 Douleur repos', '🚨 Crescendo', '🚨 Troponine élevée', '🚨 Modifications ECG']
    },
}

def get_conseil(indice):
    """
    Récupérer conseils médicaux pour une maladie
    
    Args:
        indice (int): Index maladie (0-48)
    
    Returns:
        dict: Conseils complets
    """
    if indice in CONSEILS:
        return CONSEILS[indice]
    else:
        return {
            'urgence': '⚠️ Consulter un médecin rapidement',
            'immediate': 'Repos et surveillance symptômes',
            'autosoins': ['✓ Repos', '✓ Hydratation 2L/jour', '✓ Surveillance température', '✓ Consultation si aggravation'],
            'nutrition': ['Alimentation équilibrée', 'Hydratation', 'Éviter alcool tabac'],
            'reprise': ['Consultation médicale obligatoire', 'Suivi professionnel', 'Arrêt travail si nécessaire'],
            'signes_alerte': ['🚨 Fièvre > 38.5°C', '🚨 Aggravation', '🚨 Signes vitaux anormaux', '🚨 Douleur intense']
        }
