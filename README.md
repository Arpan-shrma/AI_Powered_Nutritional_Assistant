# AI-Powered Nutritional Assistant 🍽️

## Project Overview

The AI-Powered Nutritional Assistant is a web application that helps users track their dietary habits using advanced AI technologies. The application combines computer vision for food recognition with personalized nutritional analysis and allergen detection. It is designed to integrate seamlessly with Firebase for user authentication and data storage.

## Features

* 📸 Photo-based food recognition using YOLO model
* 📊 Detailed nutritional analysis
* ⚠️ Allergen detection and alerts
* 📈 Personalized dietary tracking
* 📱 Interactive dashboard
* 📅 Meal history and statistics
* 🎯 Custom calorie goals

## Tech Stack

* Frontend: Streamlit
* Backend: Python
* Database: Firebase/Firestore
* AI/ML: YOLO, Computer Vision
* Authentication: Firebase Auth
* Visualization: Plotly
* Image Processing: OpenCV, Albumentations

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

### Prerequisites

* Python 3.8+
* Firebase account and project
* YOLO model trained on Food-101 dataset

To set up this project, follow these steps:

1. **Clone the repository:**
      ```bash
      git clone https://github.com/Arpan-shrma/AI_Powered_Nutritional_Assistant.git
      ```
2.	**Install the required dependencies:**
      ```bash
      pip install -r requirements.txt
      ```
3. **Configure Firebase:**

   * Create a Firebase project
   * Download Firebase configuration file
   * Place it in config/firebase_config.json

4. **Set up environment variables:**

   * Create a .env file in the root directory
   * Add required configurations:
     ``` env
     FIREBASE_API_KEY=your-api-key
     FIREBASE_AUTH_DOMAIN=your-domain
     FIREBASE_PROJECT_ID=your-project-id
     OPENAI_API_KEY=your-openai-key
     ```
5. **Trained YOLO model:**
   * You can use the model provided in the repository.
   * You can also use train_model.pynb to train your own model and play with the parameters to get better model.
   * Put your trained model file (best.pt) in the models/ directory     

## Usage

1. **Run the web app**
   * To run the application, execute the following command from the project root directory:
     ```bash
     streamlit run app.py
     ```
2. **Account Creation and Login**

   * Sign up with email and password
   * Provide basic information (name, height, weight)
   * Set dietary preferences and allergens

3. **Food Analysis**

   * Upload a photo of your meal
   * Click "Analyze" to process the image
   * Review the detected food and nutritional information
   * Adjust serving size if needed
   * Save the meal to your history

4. **Tracking and Analytics**

   * View daily calorie intake
   * Track nutritional metrics (protein, carbs, fat, fiber)
   * Monitor allergen exposure
   * Analyze meal patterns and trends

5. **Customization**
   * Set daily calorie goals
   * Update allergen information
   * Modify dietary preferences
   * Export nutrition data


## Application Architecture

### Core Components

1. **Model Manager** (`model_manager.py`)
   - Handles YOLO model loading and predictions
   - Manages image processing pipeline

2. **Database Manager** (`database.py`)
   - Manages Firestore interactions
   - Handles data storage and retrieval
   - Processes user analytics

3. **Authentication Manager** (`firebase_config.py`)
   - Handles user authentication
   - Manages user profiles
   - Controls access permissions

4. **Visualization Manager** (`visualization.py`)
   - Creates interactive charts and graphs
   - Generates nutrition reports
   - Handles data visualization

### Data Flow
1. User uploads image → Image processing
2. YOLO model prediction → Food identification
3. Database query → Nutrition information
4. Analysis and visualization → User interface
5. Data storage → Firebase/Firestore

## API Reference

### Model Manager
```python
predict(image, conf=0.5)
# Returns prediction results for uploaded image
```

### Database Manager
```python
save_analysis(user_id: str, analysis_data: Dict)
get_user_analyses(user_id: str, limit: int = 10)
get_food_info(food_name: str)
```

### Visualization Manager
```python
create_daily_calorie_chart(meal_history, calorie_goal)
create_nutrition_timeline(meal_history)
create_nutritional_radar(nutrition_data)
```

## Troubleshooting

### Common Issues

1. **Image Upload Errors**
   - Ensure image format is supported (JPG, JPEG, PNG)
   - Check image size and resolution
   - Verify file permissions

2. **Authentication Issues**
   - Verify Firebase configuration
   - Check internet connection
   - Ensure valid credentials

3. **Analysis Errors**
   - Confirm model file presence
   - Check image quality
   - Verify database connection

## References

1. Food 101 dataset:
   - Bossard, L., Guillaumin, M., and Van Gool, L. (2014). Food-101 – Mining discriminative components with random forests
2. Database Creation for Nutritional and Potential allergen information:
   - U.S. Department of Agriculture. (2024). FoodData Central. Agricultural Research Service. https://fdc.nal.usda.gov/
   - Food Allergy Research & Education. (2024). Common Allergens. FARE. https://www. foodallergy.org/living-food-allergies/food-allergy-essentials/common-allergens
   - The Culinary Institute of America. (2017). The Professional Chef (10th ed.). Wiley.
   - U.S. Food and Drug Administration. (2023). Guidance for Industry: Food Labeling Guide. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-industry-food-labeling-guide
   - Page, K., & Dornenburg, A. (2008). The Flavor Bible: The Essential Guide to Culinary Creativity. Little, Brown and Company.
   - Herbst, S. T. (2013). The Food Lover’s Companion (5th ed.). Barron’s Educational Series.
   - Mishra, M., Sarkar, T., Choudhury, T. et al. Allergen30: Detecting Food Items with Possible Allergens Using Deep Learning-Based Computer Vision. Food Anal. Methods 15, 3045–3078 (2022). https://doi.org/10.1007/s12161-022-02353-9
3. Motivation to use YOLO model:
   - S. Bandyopadhyay, D. Dutta and S. Pratihar, "A Comprehensive Analysis of Fast-Food Classification Using You Only Look Once (YOLO) Model," 2024 15th International Conference on Computing Communication and Networking Technologies (ICCCNT), Kamand, India, 2024, pp. 1-6, doi: 10.1109/ICCCNT61001.2024.10724136.


## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
