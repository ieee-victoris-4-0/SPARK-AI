# -*- coding: utf-8 -*-
"""
Helper functions for loading models and displaying info
"""
import easyocr
from ultralytics import YOLO
import streamlit as st

def load_yolo_model(model_path):
    """
    Load YOLO model from path
    """
    return YOLO(model_path)

def load_ocr_reader(languages):
    """
    Initialize EasyOCR reader
    """
    return easyocr.Reader(languages)

def display_drug_info(drug_name, drug_info):
    """
    Display drug information in Streamlit
    """
    if drug_info:
        st.write(f"معلومات الدواء **{drug_name}**:")
        for key, value in drug_info.items():
            st.write(f"- {key}: {value}")
    else:
        st.write(f"لا توجد معلومات متاحة للدواء **{drug_name}**")
