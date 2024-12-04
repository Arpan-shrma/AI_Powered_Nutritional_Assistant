import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# App settings
APP_NAME = "AI-Powered Nutritional Assistant"
APP_VERSION = "1.0.0"

# Model settings
MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")
MODEL_CONFIDENCE_THRESHOLD = 0.5
DEFAULT_IMAGE_SIZE = (640, 640)

# Database settings
DATABASE_PATH = os.path.join(BASE_DIR, "data", "food101_database.json")

# Firebase config
FIREBASE_CONFIG = {
    "apiKey": "your-api-key",
    "authDomain": "your-app.firebaseapp.com",
    "projectId": "your-project-id",
    "storageBucket": "your-app.appspot.com",
    "messagingSenderId": "your-sender-id",
    "appId": "your-app-id",
    "measurementId": "your-measurement-id"
}

# OpenAI settings
OPENAI_API_KEY = "your-openai-api-key"

# Streamlit settings
STREAMLIT_CONFIG = {
    "page_title": APP_NAME,
    "page_icon": "🍽️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Visualization settings
VIZ_COLOR_SCHEME = {
    'primary': '#FF4B4B',
    'secondary': '#0068C9',
    'tertiary': '#83C9FF',
    'success': '#29B09D',
    'warning': '#FFA421',
    'error': '#FF4B4B'
}

# Logging settings
LOG_LEVEL = "INFO"
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")