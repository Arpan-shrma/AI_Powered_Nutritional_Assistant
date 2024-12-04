import albumentations as A
import cv2
import numpy as np
from PIL import Image
import torch
import io
import base64

def get_augmentation_pipeline(augmentation_strength='medium'):
    """Get augmentation pipeline based on strength level"""
    base_pipeline = [
        A.Resize(640, 640, always_apply=True),
        A.OneOf([
            A.RandomCrop(width=620, height=620, p=0.5),
            A.CenterCrop(width=620, height=620, p=0.5),
        ], p=0.5),
    ]
    
    augmentation_map = {
        'light': [
            A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.1, p=0.5),
            A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=15, val_shift_limit=10, p=0.3),
            A.GaussNoise(var_limit=(10.0, 30.0), p=0.2),
            A.Rotate(limit=10, p=0.2),
        ],
        'medium': [
            A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.5),
            A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, p=0.4),
            A.GaussNoise(var_limit=(10.0, 50.0), p=0.3),
            A.Rotate(limit=15, p=0.3),
            A.RandomShadow(p=0.2),
            A.CLAHE(p=0.3),
            A.GaussianBlur(blur_limit=(3, 5), p=0.2),
        ],
        'strong': [
            A.RandomBrightnessContrast(brightness_limit=0.3, contrast_limit=0.3, p=0.6),
            A.HueSaturationValue(hue_shift_limit=30, sat_shift_limit=40, val_shift_limit=30, p=0.5),
            A.GaussNoise(var_limit=(10.0, 80.0), p=0.4),
            A.Rotate(limit=20, p=0.4),
            A.RandomShadow(p=0.3),
            A.CLAHE(p=0.4),
            A.GaussianBlur(blur_limit=(3, 7), p=0.3),
            A.Perspective(scale=(0.05, 0.1), p=0.2),
            A.ColorJitter(p=0.3),
        ]
    }
    
    selected_augmentations = base_pipeline + augmentation_map[augmentation_strength]
    return A.Compose(selected_augmentations)

def preprocess_image(image, augment=False, aug_pipeline=None):
    """Preprocess image for model input"""
    img = np.array(image)
    
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    if augment and aug_pipeline:
        augmented = aug_pipeline(image=img)
        img = augmented['image']
    
    img = cv2.resize(img, (640, 640))
    return img

def batch_process_image(image, model, num_augmentations=3, confidence_threshold=0.5, augmentation_strength='medium'):
    """Process image with batch augmentations and confidence filtering"""
    predictions = []
    confidences = []
    filtered_predictions = []
    filtered_confidences = []
    augmented_images = []
    
    # Process original image
    results = model(image)
    result = results[0]  # Get first result
    
    # Extract predictions
    if len(result.boxes) > 0:
        # Get the prediction with highest confidence
        box = result.boxes[0]  # Get first box
        pred_class = int(box.cls[0])  # Get class index
        conf = float(box.conf[0])  # Get confidence
        pred = result.names[pred_class]  # Get class name
        
        if conf >= confidence_threshold:
            filtered_predictions.append(pred)
            filtered_confidences.append(conf)
        
        predictions.append(pred)
        confidences.append(conf)
        augmented_images.append(image)
    
    # Process augmented versions if needed
    aug_pipeline = get_augmentation_pipeline(augmentation_strength)
    img_array = np.array(image)
    
    for _ in range(num_augmentations):
        augmented = aug_pipeline(image=img_array)['image']
        results = model(augmented)
        result = results[0]
        
        if len(result.boxes) > 0:
            box = result.boxes[0]
            pred_class = int(box.cls[0])
            conf = float(box.conf[0])
            pred = result.names[pred_class]
            
            if conf >= confidence_threshold:
                filtered_predictions.append(pred)
                filtered_confidences.append(conf)
            
            predictions.append(pred)
            confidences.append(conf)
            augmented_images.append(Image.fromarray(augmented))
    
    if filtered_predictions:
        max_conf_idx = np.argmax(filtered_confidences)
        final_prediction = filtered_predictions[max_conf_idx]
        final_confidence = filtered_confidences[max_conf_idx]
    elif predictions:
        max_conf_idx = np.argmax(confidences)
        final_prediction = predictions[max_conf_idx]
        final_confidence = confidences[max_conf_idx]
    else:
        final_prediction = None
        final_confidence = 0.0
    
    return final_prediction, final_confidence, predictions, confidences, augmented_images

def image_to_base64(image):
    """Convert PIL Image to base64 string"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()