# AI-Powered Nutritional Assistant

## Project Overview

This AI-Powered Nutritional Assistant helps users identify foods and track their nutritional intake using image recognition and a comprehensive food database. It is designed to integrate seamlessly with Firebase for user authentication and data storage.

## Project Structure


```plaintext
AI_Powered_Nutritional_Assistant/
├── app.py                      # Main Python file running the app
├── config/                     # Configuration files
│   ├── firebase_config.json    # Firebase configuration settings
│   └── settings.py             # General app settings
├── models/                     # Machine learning models
│   └── best.pt                 # Pre-trained model for image recognition
├── data/                       # Data resources
│   └── food101_database.json   # Database containing food information
├── utils/                      # Utility scripts
│   ├── auth.py                 # Authentication functions
│   ├── image_processing.py     # Image processing utilities
│   ├── database.py             # Database interaction functions
│   └── visualization.py        # Visualization tools
└── requirements.txt            # Dependencies required to run the app
```
## Installation

To set up this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI_Powered_Nutritional_Assistant.git
   ```
2.	Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

To run the application, execute the following command from the project root directory:
```bash
python app.py
```
