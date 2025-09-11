from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from ultralytics import YOLO
import easyocr

<<<<<<< HEAD
# Import your OCR functions
from modules.text_extraction import extract_text_with_yolo, clean_extracted_texts

# Load YOLO object detection model
=======
# Call your OCR code
from modules.text_extraction import extract_text_with_yolo, clean_extracted_texts

# Load the Object Detection model
>>>>>>> 3e2b0cfe07bfeb5b5857c2c5940403d751001da1
det_model = YOLO("models/best.pt")

# Load OCR reader (English + Arabic)
ocr_reader = easyocr.Reader(["en", "ar"])

# Initialize FastAPI app
app = FastAPI(title="Medicine Detection + OCR API")

@app.post("/predict_medicine")
async def predict_medicine(file: UploadFile = File(...)):
<<<<<<< HEAD
    # Convert uploaded image from bytes to OpenCV format
=======
    # Convert the image from bytes to OpenCV format
>>>>>>> 3e2b0cfe07bfeb5b5857c2c5940403d751001da1
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

<<<<<<< HEAD
    # Run OCR with YOLO detection
=======
    # Run OCR with YOLO
>>>>>>> 3e2b0cfe07bfeb5b5857c2c5940403d751001da1
    texts = extract_text_with_yolo(det_model, ocr_reader, img, conf_threshold=0.5)
    cleaned_texts = clean_extracted_texts(texts)

    return JSONResponse(content={"texts": cleaned_texts})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Api.deploy_fastapi:app", host="0.0.0.0", port=8000, reload=True)
