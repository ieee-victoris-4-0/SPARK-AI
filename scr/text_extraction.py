# -*- coding: utf-8 -*-
"""
Text Extraction Module
"""

import cv2
import easyocr
import re
import os
from scr.image_processing import save_image_temp


def extract_text_with_yolo(model, reader, image, conf_threshold=0.5):
    """
    Extract text using YOLO for detection and EasyOCR for recognition.
    - model: YOLO object detection model
    - reader: EasyOCR reader
    - image: input OpenCV image
    - conf_threshold: confidence threshold for YOLO
    """
    texts = []
    temp_path = save_image_temp(image)

    try:
        results = model.predict(temp_path, verbose=False)

        # Loop over YOLO results
        for r in results:
            for box in r.boxes:
                conf = box.conf[0].cpu().numpy()

                if conf >= conf_threshold:
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)

                    # Crop detected region
                    crop = image[y1:y2, x1:x2]

                    # Run OCR on cropped region
                    result = reader.readtext(crop, detail=0)
                    texts.extend(result)
    finally:
        # Delete temp file after prediction
        if os.path.exists(temp_path):
            os.unlink(temp_path)

    return texts


def clean_extracted_texts(texts):
    """
    Clean extracted texts for better matching:
    - Convert to lowercase
    - Remove non-alphabetic characters
    - Strip extra spaces
    - Keep words longer than 2 chars
    """
    cleaned = []
    for t in texts:
        t = t.lower()
        t = re.sub(r'[^a-z\s]', '', t)
        t = t.strip()
        if t and len(t) > 2:
            cleaned.append(t)
    return cleaned


if __name__ == "__main__":
    # Simple test (without YOLO/EasyOCR)
    sample_texts = ["Panadol® 500mg", "IBUPROFEN!!", "ok", "12"]
    cleaned = clean_extracted_texts(sample_texts)
    print("Original texts:", sample_texts)
    print("Cleaned texts:", cleaned)
