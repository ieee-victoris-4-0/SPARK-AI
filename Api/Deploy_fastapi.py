from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from ultralytics import YOLO
import easyocr
import sys
import os

# Add the parent directory to sys.path to access 'scr' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import OCR functions from scr folder
from scr.text_extraction import extract_text_with_yolo, clean_extracted_texts

# Load the Object Detection model
det_model = YOLO("../models/best.pt")  # Path relative to api folder

# Load OCR reader (English + Arabic)
ocr_reader = easyocr.Reader(["en", "ar"])

# Initialize FastAPI app
app = FastAPI(title="Medicine Detection + OCR API")

@app.post("/predict_medicine")
async def predict_medicine(file: UploadFile = File(...)):
    # Convert uploaded image from bytes to OpenCV format
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Run OCR with YOLO
    texts = extract_text_with_yolo(det_model, ocr_reader, img, conf_threshold=0.5)
    cleaned_texts = clean_extracted_texts(texts)

    return JSONResponse(content={"texts": cleaned_texts})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Api.Deploy_fastapi:app", host="0.0.0.0", port=8000, reload=True)
