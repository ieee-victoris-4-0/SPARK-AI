# -*- coding: utf-8 -*-
"""
إعدادات التطبيق - Configuration Settings
"""

# Model path (relative path from project root)
MODEL_PATH = "models/best.pt"

# إعدادات OCR
OCR_LANGUAGES = ['en']

# إعدادات المطابقة
MATCH_THRESHOLD = 70
CONFIDENCE_THRESHOLD = 0.5

# APIs
FDA_API_URL = "https://api.fda.gov/drug/label.json"


# -*- coding: utf-8 -*-
"""
Configuration Settings
"""

# Model path
MODEL_PATH = "models/best.pt"

# OCR settings
OCR_LANGUAGES = ['en']

# Matching settings
MATCH_THRESHOLD = 70
CONFIDENCE_THRESHOLD = 0.5

# APIs
FDA_API_URL = "https://api.fda.gov/drug/label.json"

# Drug dictionary
DRUG_DICTIONARY = [
    # Analgesics / Pain killers
    "paracetamol", "acetaminophen", "tylenol", "panadol",
    "ibuprofen", "advil", "nurofen", "diclofenac", "voltaren",
    "aspirin", "cardiprin", "naproxen", "aleve", "celecoxib", "celebrex",
    
    # Antibiotics
    "amoxicillin", "augmentin", "amoxil",
    "ciprofloxacin", "cipro",
    "clindamycin", "cephalexin", "keflex",
    "azithromycin", "zithromax",
    "clarithromycin", "biaxin",
    "doxycycline",
    "metronidazole", "flagyl",
    
    # Antihistamines
    "loratadine", "claritin",
    "cetirizine", "zyrtec",
    "fexofenadine", "allegra",
    
    # Gastro / Heartburn
    "omeprazole", "prilosec", "losec",
    "esomeprazole", "nexium",
    "pantoprazole", "protonix",
    "ranitidine", "zantac",
    "famotidine", "pepcid",
    
    # Diabetes
    "metformin", "glucophage",
    "glyburide", "glibenclamide",
    "insulin", "lantus", "humalog",
    
    # Cardiovascular
    "lipitor", "atorvastatin",
    "simvastatin", "zocor",
    "pravastatin", "pravachol",
    "rosuvastatin", "crestor",
    "metoprolol", "lopressor",
    "atenolol", "tenormin",
    "amlodipine", "norvasc",
    "losartan", "cozaar",
    
    # Corticosteroids
    "prednisone",
    "hydrocortisone",
    "methylprednisolone",
    
    # Antidepressants / Mental Health
    "amitriptyline",
    "sertraline", "zoloft",
    "fluoxetine", "prozac",
    "paroxetine", "paxil",
    "citalopram", "celexa",
    
    # Blood / Anticoagulants
    "warfarin", "coumadin",
    "heparin",
    
    # Others
    "fleboral", "fleboral forte",
    "omeprazole magnesium",
    "ranitidine bismuth citrate",
    "tramadol", "ultram",
    "gabapentin", "neurontin",
    "lisinopril", "prinivil", "zestril",
    "clopidogrel", "plavix",
    "allopurinol", "zyloprim",
    "levothyroxine", "synthroid"
]
