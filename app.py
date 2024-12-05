import streamlit as st
from utils.firebase_config import AuthManager
from utils.database import DatabaseManager
from utils.visualization import VisualizationManager
from PIL import Image
import plotly.graph_objects as go
from datetime import datetime, time
import time
from ultralytics import YOLO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize managers
auth_manager = AuthManager()
db_manager = DatabaseManager()
viz_manager = VisualizationManager()

# Load YOLO model with caching
@st.cache_resource
def load_model():
    try:
        model = YOLO('models/best.pt')
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Configure page
st.set_page_config(
    page_title="AI-Powered Nutritional Assistant",
    page_icon="🍽️",
    layout="wide"
)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'model' not in st.session_state:
    st.session_state.model = load_model()
if 'prediction_data' not in st.session_state:
    st.session_state.prediction_data = None
if 'current_food_info' not in st.session_state:
    st.session_state.current_food_info = None
if 'current_prediction' not in st.session_state:
    st.session_state.current_prediction = None
if 'current_confidence' not in st.session_state:
    st.session_state.current_confidence = None
if 'calorie_goal' not in st.session_state:
    st.session_state.calorie_goal = 2000
if 'meal_history' not in st.session_state:
    st.session_state.meal_history = []
if 'serving_nutrition' not in st.session_state:
    st.session_state.serving_nutrition = None
if 'last_uploaded_file' not in st.session_state:
    st.session_state.last_uploaded_file = None

def get_calorie_goal(user_profile):
    """Get user's calorie goal from profile or set default"""
    if 'calorie_goal' not in st.session_state:
        st.session_state.calorie_goal = user_profile.get('calorie_goal', 2000)
    return st.session_state.calorie_goal

def calculate_calories_for_serving(base_calories, serving_size_g):
    """Calculate calories for given serving size"""
    return (base_calories * serving_size_g) / 100

def get_todays_calories(meal_history):
    """Calculate total calories consumed today"""
    today = datetime.now().date()
    today_meals = [
        meal for meal in meal_history 
        if meal['timestamp'].date() == today
    ]
    return sum(meal['calories'] for meal in today_meals)

def reset_analysis_state():
    """Reset all analysis-related session states"""
    st.session_state.prediction_data = None
    st.session_state.current_food_info = None
    st.session_state.current_prediction = None
    st.session_state.current_confidence = None
    st.session_state.serving_nutrition = None
    st.session_state.last_uploaded_file = None

def analyze_food(image):
    """Analyze food image and return prediction"""
    try:
        # Reset serving nutrition when starting new analysis
        st.session_state.serving_nutrition = None
        
        image = image.resize((640, 640))
        results = st.session_state.model(image)
        
        if results and len(results) > 0:
            result = results[0]
            probs = result.probs
            
            if probs is not None:
                st.session_state.prediction_data = result
                prediction = result.names[probs.top1]
                confidence = float(probs.top1conf)
                st.session_state.current_prediction = prediction
                return prediction, confidence
        
        return None, 0.0
        
    except Exception as e:
        st.error(f"Error analyzing image: {str(e)}")
        return None, 0.0

def update_meal_history():
    """Update meal history in session state"""
    if st.session_state.authenticated and st.session_state.user_id:
        st.session_state.meal_history = db_manager.get_user_analyses(st.session_state.user_id)

def main():
    st.title("🍽️ AI-Powered Nutritional Assistant")
    if not st.session_state.authenticated:
        tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
        
        with tab1:
            with st.form("signin_form"):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                signin_submitted = st.form_submit_button("Sign In")
                
                if signin_submitted:
                    user_id, error = auth_manager.sign_in(email, password)
                    if user_id:
                        st.session_state.user_id = user_id
                        st.session_state.authenticated = True
                        update_meal_history()
                        st.rerun()
                    else:
                        st.error(f"Sign in failed: {error}")
        
        with tab2:
            with st.form("signup_form"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                confirm_password = st.text_input("Confirm Password", type="password")
                height = st.number_input("Height (cm)", min_value=0)
                weight = st.number_input("Weight (kg)", min_value=0)
                signup_submitted = st.form_submit_button("Sign Up")
                
                if signup_submitted:
                    if password != confirm_password:
                        st.error("Passwords don't match!")
                    else:
                        user_id, error = auth_manager.sign_up(
                            email, password, name, height, weight
                        )
                        if user_id:
                            st.success("Account created successfully! Please sign in.")
                        else:
                            st.error(f"Sign up failed: {error}")
    
    else:
        user_profile = auth_manager.get_user_profile(st.session_state.user_id)
        if not st.session_state.meal_history:
            update_meal_history()
        
        # Sidebar
        with st.sidebar:
            st.title("Profile")
            st.write(f"Welcome, {user_profile['name']}")
            
            current_goal = get_calorie_goal(user_profile)
            new_goal = st.number_input(
                "Daily Calorie Goal", 
                min_value=1000, 
                max_value=5000, 
                value=int(current_goal)
            )
            
            if new_goal != current_goal:
                st.session_state.calorie_goal = new_goal
                auth_manager.update_user_profile(st.session_state.user_id, {'calorie_goal': new_goal})
                st.success("Calorie goal updated!")
            
            # Add a divider
            st.divider()
            
            # Today's Calorie Summary
            st.subheader("Today's Calories")
            
            # Get today's meals only
            today = datetime.now().date()
            todays_meals = [
                meal for meal in st.session_state.meal_history 
                if meal['timestamp'].date() == today
            ]
            
            # Calculate today's calories from saved meals
            today_calories = sum(meal['calories'] for meal in todays_meals)
            
            # Only add current meal calories if actively analyzing
            if (st.session_state.current_food_info and 
                st.session_state.current_prediction and 
                st.session_state.serving_nutrition):
                today_calories += st.session_state.serving_nutrition['calories']
            
            calories_remaining = st.session_state.calorie_goal - today_calories
            
            if todays_meals or (st.session_state.current_food_info and st.session_state.serving_nutrition):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Consumed", f"{today_calories:.0f} kcal")
                with col2:
                    st.metric("Remaining", f"{calories_remaining:.0f} kcal")
                
                # Progress bar
                progress = min(today_calories / st.session_state.calorie_goal, 1.0)
                st.progress(progress, text="Daily Progress")
            else:
                st.info("No meals logged today")
            
            st.divider()
            
            user_allergens = st.multiselect(
                "Your Allergens",
                ["lactose", "nuts", "gluten", "shellfish", "eggs", "salicylate", "soy", "histamine"],
                default=user_profile.get('allergens', [])
            )
            if st.button("Update Allergens"):
                auth_manager.update_allergens(st.session_state.user_id, user_allergens)
                st.success("Allergens updated!")
            
            if st.button("Sign Out"):
                st.session_state.clear()
                st.rerun()
        # Main content tabs
        tab1, tab2, tab3 = st.tabs(["Food Analysis", "History", "Statistics"])
        
        with tab1:
            st.header("Food Analysis")
            if st.button("Upload New Meal", type="primary"):
                reset_analysis_state()
                st.rerun()
                
            uploaded_file = st.file_uploader("Upload your meal photo", type=["jpg", "jpeg", "png"])
            
            if uploaded_file:
                # Reset analysis state when new file is uploaded
                if st.session_state.last_uploaded_file != uploaded_file:
                    reset_analysis_state()
                    st.session_state.last_uploaded_file = uploaded_file
                
                image = Image.open(uploaded_file)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.image(image, caption="Your Meal", use_container_width=True)
                
                with col2:
                    analyze_clicked = st.button("Analyze")
                    if analyze_clicked:
                        if st.session_state.model is None:
                            st.error("Model not loaded. Please try again later.")
                        else:
                            with st.spinner("Analyzing your meal..."):
                                prediction, confidence = analyze_food(image)
                                if prediction and confidence >= 0.5:
                                    food_info = db_manager.get_food_info(prediction)
                                    st.session_state.current_food_info = food_info
                                    st.session_state.current_prediction = prediction
                                    st.session_state.current_confidence = confidence
            
            if st.session_state.current_food_info and st.session_state.current_prediction:
                food_info = st.session_state.current_food_info
                current_prediction = st.session_state.current_prediction
                current_confidence = st.session_state.current_confidence
                
                st.success(f"Detected: {current_prediction.replace('_', ' ').title()}")
                st.info(f"Confidence: {current_confidence:.2%}")
                
                dangerous_allergens = set(food_info['allergens']) & set(user_allergens)
                if dangerous_allergens:
                    st.error("⚠️ Allergen Alert!")
                    st.write("This meal contains:", ", ".join(dangerous_allergens))
                else:
                    st.success("✅ Safe for your dietary restrictions!")

                with st.expander("See all predictions"):
                    if st.session_state.prediction_data:
                        top_indices = st.session_state.prediction_data.probs.top5
                        top_confs = st.session_state.prediction_data.probs.top5conf
                        for idx, conf in zip(top_indices, top_confs):
                            st.write(f"{st.session_state.prediction_data.names[idx]}: {float(conf):.2%}")

                st.subheader("Calculate Calories")
                default_serving = float(food_info['serving_size'].split('(')[-1].strip('g)'))
                st.write(f"Standard serving: {food_info['serving_size']}")
                serving_size = st.number_input(
                    "Your serving size (grams)",
                    min_value=1,
                    max_value=1000,
                    value=int(default_serving),
                    help="Enter your portion size in grams",
                    key="serving_size_input"
                )

                calculate_clicked = st.button("Calculate Nutrition", key="calc_nutrition")
                
                if calculate_clicked:
                    base_nutrition = food_info['nutrition_per_100g']
                    st.session_state.serving_nutrition = {
                        'calories': calculate_calories_for_serving(base_nutrition['calories'], serving_size),
                        'protein': (base_nutrition['protein'] * serving_size) / 100,
                        'carbs': (base_nutrition['carbs'] * serving_size) / 100,
                        'fat': (base_nutrition['fat'] * serving_size) / 100,
                        'fiber': (base_nutrition['fiber'] * serving_size) / 100
                    }

                # Show nutrition information if it exists
                if st.session_state.serving_nutrition:
                    st.subheader("Nutrition Information")
                    col1, col2 = st.columns(2)
                    with col1:
                        metrics = viz_manager.format_metrics(st.session_state.serving_nutrition)
                        for key, value in metrics.items():
                            st.metric(key, value)
                    with col2:
                        st.plotly_chart(
                            viz_manager.create_nutritional_radar(st.session_state.serving_nutrition),
                            use_container_width=True,
                            key="analysis_nutrition_radar"
                        )

                    daily_total = get_todays_calories(st.session_state.meal_history) + st.session_state.serving_nutrition['calories']
                    calories_remaining = st.session_state.calorie_goal - daily_total
                    if calories_remaining > 0:
                        st.success(f"🎯 {calories_remaining:.0f} calories remaining today")
                    else:
                        st.warning(f"⚠️ {abs(calories_remaining):.0f} calories over your daily goal")

                    # Save meal button outside the calculate_clicked condition
                    save_clicked = st.button("Save Meal", key="save_meal")
                    if save_clicked:
                        analysis_data = {
                            'food_name': current_prediction,
                            'serving_size': serving_size,
                            'calories': st.session_state.serving_nutrition['calories'],
                            'protein': st.session_state.serving_nutrition['protein'],
                            'carbs': st.session_state.serving_nutrition['carbs'],
                            'fat': st.session_state.serving_nutrition['fat'],
                            'fiber': st.session_state.serving_nutrition['fiber'],
                            'allergens': food_info['allergens'],
                            'has_allergens': bool(dangerous_allergens),
                            'allergic_ingredients': list(dangerous_allergens),
                            'timestamp': datetime.now()
                        }
                        
                        if db_manager.save_analysis(st.session_state.user_id, analysis_data):
                            # Force update meal history from database
                            update_meal_history()
                            st.success("Meal saved successfully!")
                            reset_analysis_state()  # Reset after successful save
                            # Delay rerun to show success message
                            time.sleep(5)
                            st.rerun()
                        else:
                            st.error("Failed to save meal. Please try again.")

        with tab2:
            st.header("Meal History")
            if st.session_state.meal_history:
                meal_history = sorted(st.session_state.meal_history, key=lambda x: x['timestamp'], reverse=True)
                for idx, meal in enumerate(meal_history):
                    nutrition_data = {
                        'calories': meal.get('calories', 0),
                        'protein': meal.get('protein', 0),
                        'carbs': meal.get('carbs', 0),
                        'fat': meal.get('fat', 0),
                        'fiber': meal.get('fiber', 0)
                    }
                    
                    with st.expander(f"{meal['food_name']} - {meal['timestamp'].strftime('%Y-%m-%d %H:%M')}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            metrics = viz_manager.format_metrics(nutrition_data)
                            for key, value in metrics.items():
                                st.metric(key, value)
                        with col2:
                            st.plotly_chart(
                                viz_manager.create_nutritional_radar(nutrition_data),
                                use_container_width=True,
                                key=f"history_radar_{meal['timestamp'].strftime('%Y%m%d%H%M%S')}_{idx}"
                            )
                        
                        if meal.get('has_allergens'):
                            st.error(f"⚠️ This meal contained allergens: {', '.join(meal['allergic_ingredients'])}")

        with tab3:
            st.header("Nutrition Statistics")
            if st.session_state.meal_history:
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(
                        viz_manager.create_meal_distribution(st.session_state.meal_history),
                        use_container_width=True,
                        key="stats_meal_distribution"
                    )
                with col2:
                    st.plotly_chart(
                        viz_manager.create_allergen_exposure_chart(st.session_state.meal_history),
                        use_container_width=True,
                        key="stats_allergen_exposure"
                    )
                
                st.plotly_chart(
                    viz_manager.create_nutrition_timeline(st.session_state.meal_history),
                    use_container_width=True,
                    key="stats_nutrition_timeline"
                )
                
                st.plotly_chart(
                    viz_manager.create_weekly_summary(st.session_state.meal_history, st.session_state.calorie_goal),
                    use_container_width=True,
                    key="stats_weekly_summary"
                )

                # Monthly trends (if applicable)
                if len(st.session_state.meal_history) > 7:
                    st.subheader("Monthly Trends")
                    st.plotly_chart(
                        viz_manager.create_nutrition_timeline(st.session_state.meal_history),
                        use_container_width=True,
                        key="stats_monthly_trends"
                    )

if __name__ == "__main__":
    main()