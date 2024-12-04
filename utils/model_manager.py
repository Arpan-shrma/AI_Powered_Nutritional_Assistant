import streamlit as st
from ultralytics import YOLO
from pathlib import Path

class ModelManager:
    def __init__(self):
        self.model = self.load_model()

    @st.cache_resource
    def load_model(self):
        """Load and cache the trained YOLO model"""
        try:
            # Load trained YOLO model
            model = YOLO('models/best.pt')
            return model
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None

    def predict(self, image, conf=0.5):
        """
        Make prediction on an image
        Args:
            image: PIL Image or numpy array
            conf: confidence threshold
        Returns:
            prediction results
        """
        if self.model is None:
            return None
        
        try:
            # Use the trained model for prediction
            results = self.model(image, conf=conf)
            return results[0]
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")
            return None