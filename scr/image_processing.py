# -*- coding: utf-8 -*-
"""
Image Processing Module
"""

import cv2
import numpy as np
import tempfile
import os
from PIL import Image


def capture_image_from_camera():
    """
    Capture image from camera using Streamlit
    """
    import streamlit as st
    img_file_buffer = st.camera_input("Capture a photo of the medicine package")

    if img_file_buffer is not None:
        # Convert image buffer to OpenCV format
        bytes_data = img_file_buffer.getvalue()
        img_array = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return img
    return None


def upload_image():
    """
    Upload image from device using Streamlit
    """
    import streamlit as st
    uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        # Convert file to OpenCV format
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        return image
    return None


def save_image_temp(image):
    """
    Save image temporarily for prediction
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_path = temp_file.name
    temp_file.close()

    cv2.imwrite(temp_path, image)
    return temp_path


def preprocess_image_for_ocr(image):
    """
    Preprocess image for better OCR accuracy
    - Convert to grayscale
    - Apply Otsu thresholding
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh


if __name__ == "__main__":
    # Test the module functionality
    dummy_img = np.zeros((200, 200, 3), dtype=np.uint8)

    # Save image temporarily
    path = save_image_temp(dummy_img)
    print(f"Temporary image saved at: {path}")

    # Preprocess image
    processed = preprocess_image_for_ocr(dummy_img)
    print("Preprocessing done. Shape:", processed.shape)

    # Remove temporary file
    if os.path.exists(path):
        os.remove(path)
        print("Temporary file deleted.")
