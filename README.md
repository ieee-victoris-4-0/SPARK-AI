# SPARK AI - Drug Name Detection System

![SPARK AI Logo](Training_set_samples.png)

## 🚀 Overview
SPARK AI is an advanced drug name detection system that combines YOLOv8 object detection with OCR technology to accurately identify and extract drug names from medication packaging. Developed by the SPARK AI team, this system achieves state-of-the-art performance with 88.7% mAP50 accuracy.

## 📊 Performance Highlights
- *mAP50*: 0.8870
- *mAP50-95*: 0.6087  
- *Precision*: 0.8758
- *Recall*: 0.8352
- *Inference Speed*: 170.2ms per image

## 🏗 Project Structure

SPARK_AI/
│
├── Api/                          # FastAPI deployment code
│   └── deploy_fastapi.py         # API deployment script
│
├── __pycache__/                  # Python cache files
│
├── dataset/                      # Dataset directory
│   ├── data.yaml                 # Dataset configuration
│   ├── train/                    # Training data
│   ├── test/                     # Testing data  
│   └── valid/                    # Validation data
│
├── model/                        # Model files
│   └── best.pt                   # Trained YOLOv8 model
│
├── notebook/                     # Jupyter notebooks
│   ├── Drug_Name_Detection_and_OCR_Pipeline.ipynb
│   └── Pharmaceutical_Drug_Name_Detection.ipynb
│
├── scr/                          # Source code (main application)
│   ├── __init__.py
│   ├── ocr/                      # OCR processing modules
│   └── utils/                    # Utility functions
│
├── utils/                        # Additional utilities
│
├── README.md                     # This documentation file
├── Training_set_samples.png      # Training data visualization
├── Visualizing_predictions_on_test_images.png  # Test results
├── image_through_the_complete_pipeline.png     # Full pipeline example
├── config.py                     # Configuration settings
├── main.py                       # Main application entry point
└── requirements.txt              # Python dependencies


## 🖼 Visual Results

### Training Samples
![Training Samples](Training_set_samples.png)
Example training images with annotated drug name regions from our dataset

### Test Predictions  
![Test Predictions](Visualizing_predictions_on_test_images.png)
Model predictions on test images showing accurate bounding boxes and confidence scores

### Complete Pipeline
![Complete Pipeline](image_through_the_complete_pipeline.png)
End-to-end pipeline demonstrating original image, YOLOv8 detection, region cropping, and OCR text extraction

## 🛠 Installation

bash
# Clone repository (when available)
# git clone https://github.com/spark-team/SPARK_AI.git
cd SPARK_AI

# Install dependencies
pip install -r requirements.txt


## 🚀 Quick Start

### Command Line Interface
bash
# Single image processing
python main.py --image path/to/medicine.jpg

# Batch processing  
python main.py --folder path/to/medicines/ --confidence 0.6

# Using custom model
python main.py --image medicine.jpg --model_path model/best.pt


### API Deployment
bash
# Start FastAPI server
python Api/deploy_fastapi.py

# API will be available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs


### Example API Usage
bash
# Detect drug name from image
curl -X POST -F "image=@medicine.jpg" http://localhost:8000/detect

# Get health status
curl http://localhost:8000/health


## 📖 Usage Examples

### Python Integration
python
from scr.ocr.text_extraction import DrugDetector

# Initialize detector
detector = DrugDetector(confidence_threshold=0.6)

# Single image processing
result = detector.process_image("medicine.jpg")
print(f"Detected: {result['text']} (Confidence: {result['confidence']:.3f})")

# Batch processing
results = detector.process_batch(["med1.jpg", "med2.jpg"])


## 🧩 Core Modules

### 1. Object Detection (YOLOv8)
- *Model*: model/best.pt (custom trained)
- *Input Size*: 640x640 pixels  
- *Confidence Threshold*: 0.5 (configurable)
- *NMS IoU Threshold*: 0.45

### 2. OCR Processing (EasyOCR)
- *Language Support*: English
- *Text Confidence Threshold*: 0.7
- *GPU Acceleration*: Supported
- *Text Validation*: Integrated

### 3. API Services (FastAPI)
- *RESTful Endpoints*: JSON API
- *Batch Processing*: Multiple image support
- *Health Monitoring*: System status checks
- *Interactive Documentation*: Auto-generated docs

## ⚡ Performance Metrics

| Operation | Time (ms) |
|-----------|-----------|
| Preprocessing | 4.0 |
| Inference | 170.2 |
| Postprocessing | 0.9 |
| OCR Extraction | 400.0 |
| *Total* | *575.1* |

## 🎯 Accuracy Results

### Detection Performance

✅ mAP50: 0.8870
✅ mAP50-95: 0.6087  
✅ Precision: 0.8758
✅ Recall: 0.8352
✅ F1 Score: 0.8550


### Sample Output
json
{
  "success": true,
  "results": [
    {
      "text": "ALLOPURINOL",
      "ocr_confidence": 0.711,
      "detection_confidence": 0.846,
      "overall_confidence": 0.778
    }
  ],
  "processing_time": 0.425
}


## 🔧 Configuration

Edit config.py to customize settings:

python
# Model settings
MODEL_CONFIG = {
    "confidence_threshold": 0.5,
    "iou_threshold": 0.45,
    "image_size": 640
}

# OCR settings
OCR_CONFIG = {
    "languages": ["en"],
    "text_threshold": 0.7,
    "gpu_acceleration": False
}


## 👥 Team

### *SPARK AI Team*
- *Hassan Abdul-razeq* - AI Research & Development
- *Mohamed Mahmoud Elseragy* - Machine Learning Engineering

### Key Contributions
- Custom YOLOv8 model training and optimization
- OCR pipeline development and integration
- API design and implementation
- Performance benchmarking and validation

## 🌟 Features

- ✅ *High Accuracy*: 88.7% mAP50 detection rate
- ✅ *Fast Processing*: ~575ms end-to-end latency
- ✅ *Batch Support*: Concurrent image processing
- ✅ *REST API*: Easy web/mobile integration
- ✅ *Configurable*: Adjustable parameters
- ✅ *Visualization*: Results with bounding boxes
- ✅ *Export*: JSON, text, and image outputs

## 🚀 Deployment Options

### Local Deployment
bash
# Production deployment
python Api/deploy_fastapi.py


### Docker Deployment (Example)
dockerfile
# Example Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "Api/deploy_fastapi.py"]


## 📈 Performance Tips

1. *Enable GPU* for faster OCR processing
2. *Adjust confidence thresholds* for precision/recall balance
3. *Use batch processing* for multiple images
4. *Resize large images* before processing
5. *Monitor system resources* during deployment

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- *Ultralytics* for YOLOv8 framework
- *EasyOCR* team for text recognition
- *OpenCV* community for image processing
- *FastAPI* team for web framework

## 📞 Support

For support and questions:
- 📧 Email: spark.ai.team@example.com
- 🐛 Issues: GitHub Issues page
- 💬 Discussions: GitHub Discussions

---

*SPARK AI* - Transforming Pharmaceutical Automation through AI 💊🤖

"Accurate drug detection for safer medication management"
