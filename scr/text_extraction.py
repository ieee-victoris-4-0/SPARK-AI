# -*- coding: utf-8 -*-
"""
 Text Extraction Module
"""
import cv2
import easyocr
import re
import os
from modules.image_processing import save_image_temp

def extract_text_with_yolo(model, reader, image, conf_threshold=0.5):
    """
 Extract text using YOLO
    """
    texts = []
    

    temp_path = save_image_temp(image)
    
    try:

        results = model.predict(temp_path, verbose=False)
        
        for r in results:
                conf = box.conf[0].cpu().numpy()
                
                if conf >= conf_threshold:
           
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                    
              
                    crop = image[y1:y2, x1:x2]
                    
           
                    result = reader.readtext(crop, detail=0)
                    texts.extend(result)
    finally:

        if os.path.exists(temp_path):
            os.unlink(temp_path)
    
    return texts

def clean_extracted_texts(texts):
    """
    تنظيف النصوص المستخرجة - Clean extracted texts
    """
    cleaned = []
    for t in texts:
        t = t.lower()  
        t = re.sub(r'[^a-z\s]', '', t)  
        t = t.strip()  
        if t and len(t) > 2:  
            cleaned.append(t)

    return cleaned
