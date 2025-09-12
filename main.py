# -*- coding: utf-8 -*-
"""
Main Application File
"""
import sys
import os

# Add project root to Python path (to find scr package)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import cv2
import numpy as np

# Import config (outside scr) and modules from scr folder
from config import MODEL_PATH, OCR_LANGUAGES
from scr.image_processing import capture_image_from_camera, upload_image
from scr.text_extraction import extract_text_with_yolo, clean_extracted_texts
from scr.drug_matching import match_drug_names
from scr.api_handler import get_drug_info_from_api
from scr.helpers import load_yolo_model, load_ocr_reader, display_drug_info


def main():
    """
    Main application function
    """
    # App title and description (Arabic UI)
    st.title("نظام التعرف على الأدوية واستخراج معلوماتها")
    st.write("التقط صورة لعلبة الدواء أو ارفع صورة موجودة")
    
    # Load YOLO model and OCR reader
    model = load_yolo_model(MODEL_PATH)
    reader = load_ocr_reader(OCR_LANGUAGES)
    
    # Image input options
    option = st.radio("اختر طريقة الإدخال:", ("الكاميرا", "رفع صورة"))
    
    image = None
    if option == "الكاميرا":
        image = capture_image_from_camera()
    else:
        image = upload_image()
    
    if image is not None:
        # Display selected image
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="الصورة المختارة", use_column_width=True)
        
        # Process image
        with st.spinner("جاري معالجة الصورة..."):
            try:
                # Extract texts using YOLO + OCR
                texts = extract_text_with_yolo(model, reader, image)
                
                # Clean extracted texts
                cleaned_texts = clean_extracted_texts(texts)
                
                # Match extracted texts with drug names
                matched_drugs = match_drug_names(cleaned_texts)
                
                # Show results
                if matched_drugs:
                    st.success("تم التعرف على الأدوية التالية:")
                    
                    for word, match, score in matched_drugs:
                        st.write(f"**{match}** (مطابقة بنسبة {score}% للنص: '{word}')")
                        
                        # Fetch drug information from API
                        drug_info = get_drug_info_from_api(match)
                        display_drug_info(match, drug_info)
                else:
                    st.error("لم يتم التعرف على أي دواء في الصورة")
                    
                    # Show extracted texts for debugging
                    if cleaned_texts:
                        st.write("النصوص المستخرجة:", ", ".join(cleaned_texts))
            
            except Exception as e:
                st.error(f"حدث خطأ أثناء معالجة الصورة: {str(e)}")


if __name__ == "__main__":
    main()
