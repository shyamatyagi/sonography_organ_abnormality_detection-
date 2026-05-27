# Sonography Abnormality Detection using U-Net and YOLO

## Overview

This project presents a comparative study of two deep learning models, **U-Net** and **YOLO**, for abnormality detection in ultrasound (sonography) images.

The objective of the project is to analyze and compare the performance of:
- **U-Net** for medical image segmentation
- **YOLO** for real-time object detection

Both models were trained and evaluated on ultrasound image datasets to identify and localize abnormalities in different organs.

---

## Objectives

- Detect abnormalities in sonography images
- Compare segmentation and object detection approaches
- Evaluate model performance using standard metrics
- Analyze strengths and limitations of both models

---

## Models Used

### 1. U-Net
U-Net is a convolutional neural network architecture designed for biomedical image segmentation.  
It was used to segment abnormal regions from ultrasound images.

### 2. YOLO (You Only Look Once)
YOLO is a real-time object detection model used for detecting and localizing abnormalities with bounding boxes.

---

## Technologies Used

- Python
- PyTorch
- OpenCV
- Ultralytics YOLO
- NumPy
- Matplotlib
- Google Colab
```

---

## Dataset



> Dataset is not included in this repository due to size limitations.

---

## Training

Both models were trained using Google Colab with GPU acceleration.

### U-Net
- Used for segmentation of abnormal regions
- Trained using annotated medical image masks

### YOLO
- Used for object detection and localization
- Trained on labeled ultrasound images with bounding box annotations

---

## Evaluation Metrics

The models were evaluated using:
- Accuracy
- Precision
- Recall
- IoU (Intersection over Union)
- Dice Score
- mAP (Mean Average Precision)

---




## Comparative Analysis

| Feature | U-Net | YOLO |
|-----------|-------------|------------------|
| Approach | Segmentation | Object Detection |
| Output   | Pixel-wise masks | Bounding boxes |
| Speed     | Moderate        | Fast |
| Localization | Detailed | Efficient |
| Real-Time Capability | Limited | High |

---

## Conclusion

This project demonstrates the application of deep learning techniques in medical image analysis using ultrasound data.

The comparative analysis showed that:
- U-Net performs well for detailed segmentation tasks
- YOLO provides faster and more accurate real-time detection for certain abnormalities

The project highlights the potential of AI-assisted diagnosis in medical imaging systems.

---

## Future Improvements

- Train on larger medical datasets
- Improve detection of smaller abnormalities
- Deploy as a web application
- Integrate real-time ultrasound analysis
- Enhance segmentation accuracy

---

## Author

Shyama
