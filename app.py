import streamlit as st
from utils.firebase_config import AuthManager
from utils.database import DatabaseManager
from utils.visualization import VisualizationManager
from PIL import Image
import plotly.graph_objects as go
from datetime import datetime
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
if 'daily_calorie_goal' not in st.session_state:
    st.session_state.daily_calorie_goal = None
if 'daily_calories' not in st.session_state:
    st.session_state.daily_calories = 0
if 'prediction_data' not in st.session_state:
    st.session_state.prediction_data = None
if 'current_food_info' not in st.session_state:
    st.session_state.current_food_info = None
if 'current_prediction' not in st.session_state:
    st.session_state.current_prediction = None
if 'current_confidence' not in st.session_state:
    st.session_state.current_confidence = None

def calculate_calories_for_serving(base_calories, serving_size_g):
    """Calculate calories for given serving size"""
    return (base_calories * serving_size_g) / 100

def get_todays_calories(meal_history):
    """Calculate total calories consumed today"""
    today_meals = [
        meal for meal in meal_history 
        if meal['timestamp'].date() == datetime.now().date()
    ]
    return sum(meal['calories'] for meal in today_meals)

def analyze_food(image):
    """Analyze food image and return prediction"""
    try:
        # Ensure consistent image size
        image = image.resize((640, 640))
        
        # Make prediction
        results = st.session_state.model(image)
        
        # Process results
        if results and len(results) > 0:
            result = results[0]
            probs = result.probs
            
            if probs is not None:
                st.session_state.prediction_data = result
                prediction = result.names[probs.top1]
                confidence = float(probs.top1conf)
                st.session_state.current_prediction = prediction  # Store current prediction
                return prediction, confidence
        
        return None, 0.0
        
    except Exception as e:
        st.error(f"Error analyzing image: {str(e)}")
        return None, 0.0

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
        meal_history = db_manager.get_user_analyses(st.session_state.user_id)
        
        # Sidebar
        with st.sidebar:
            st.title("Profile")
            st.write(f"Welcome, {user_profile['name']}")
            
            # Calorie goal setting
            current_goal = st.session_state.daily_calorie_goal or user_profile.get('calorie_goal', 2000)
            new_goal = st.number_input("Daily Calorie Goal", 
                                    min_value=1000, 
                                    max_value=5000, 
                                    value=int(current_goal))
            
            if new_goal != current_goal:
                st.session_state.daily_calorie_goal = new_goal
                auth_manager.update_user_profile(st.session_state.user_id, {'calorie_goal': new_goal})
                st.success("Calorie goal updated!")

            # Daily calorie summary
            # if meal_history:
            #     daily_total = get_todays_calories(meal_history)
            #     calories_remaining = new_goal - daily_total
            #     st.write("Today's Progress:")
            #     st.write(f"Consumed: {daily_total:.0f} kcal")
            #     if calories_remaining > 0:
            #         st.success(f"Remaining: {calories_remaining:.0f} kcal")
            #     else:
            #         st.warning(f"Over by: {abs(calories_remaining):.0f} kcal")
            
            # Allergen settings
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
            uploaded_file = st.file_uploader("Upload your meal photo", type=["jpg", "jpeg", "png"])
            
            if uploaded_file:
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
                    
                    # Show results if we have prediction data
                    if st.session_state.current_food_info and st.session_state.current_prediction:
                        food_info = st.session_state.current_food_info
                        current_prediction = st.session_state.current_prediction
                        current_confidence = st.session_state.current_confidence
                        
                        # Show all predictions first
                        with st.expander("See all predictions"):
                            if st.session_state.prediction_data:
                                top_indices = st.session_state.prediction_data.probs.top5
                                top_confs = st.session_state.prediction_data.probs.top5conf
                                for idx, conf in zip(top_indices, top_confs):
                                    st.write(f"{st.session_state.prediction_data.names[idx]}: {float(conf):.2%}")
                        
                        # Display detection results
                        st.success(f"Detected: {current_prediction.replace('_', ' ').title()}")
                        st.info(f"Confidence: {current_confidence:.2%}")
                        
                        # Rest of your code...
                        # Check for allergens
                        dangerous_allergens = set(food_info['allergens']) & set(user_allergens)
                        if dangerous_allergens:
                            st.error("⚠️ Allergen Alert!")
                            st.write("This meal contains:", ", ".join(dangerous_allergens))
                        else:
                            st.success("✅ Safe for your dietary restrictions!")

                        # Serving size input
                        st.subheader("Serving Information")
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

                        # Calculate nutrition for serving size
                        base_nutrition = food_info['nutrition_per_100g']
                        serving_nutrition = {
                            'calories': calculate_calories_for_serving(base_nutrition['calories'], serving_size),
                            'protein': (base_nutrition['protein'] * serving_size) / 100,
                            'carbs': (base_nutrition['carbs'] * serving_size) / 100,
                            'fat': (base_nutrition['fat'] * serving_size) / 100,
                            'fiber': (base_nutrition['fiber'] * serving_size) / 100
                        }

                        if st.button("Save Meal"):
                            # Save analysis
                            analysis_data = {
                                'food_name': current_prediction,
                                'serving_size': serving_size,
                                'calories': serving_nutrition['calories'],
                                'protein': serving_nutrition['protein'],
                                'carbs': serving_nutrition['carbs'],
                                'fat': serving_nutrition['fat'],
                                'fiber': serving_nutrition['fiber'],
                                'allergens': food_info['allergens'],
                                'has_allergens': bool(dangerous_allergens),
                                'allergic_ingredients': list(dangerous_allergens),
                                'timestamp': datetime.now()
                            }
                            db_manager.save_analysis(st.session_state.user_id, analysis_data)
                            st.success("Meal saved successfully!")


                        # Display nutrition information
                        st.subheader("Nutrition Information")
                        col1, col2 = st.columns(2)
                        with col1:
                            metrics = viz_manager.format_metrics(serving_nutrition)
                            for key, value in metrics.items():
                                st.metric(key, value)
                        with col2:
                            st.plotly_chart(
                                viz_manager.create_nutritional_radar(serving_nutrition),
                                use_container_width=True,
                                key="analysis_radar"
                            )

                        # Display calorie tracking
                        daily_total = get_todays_calories(meal_history) + serving_nutrition['calories']
                        calories_remaining = st.session_state.daily_calorie_goal - daily_total
                        if calories_remaining > 0:
                            st.success(f"🎯 {calories_remaining:.0f} calories remaining today")
                        else:
                            st.warning(f"⚠️ {abs(calories_remaining):.0f} calories over your daily goal")
        
        with tab2:
            st.header("Meal History")
            if meal_history:
                meal_history = sorted(meal_history, key=lambda x: x['timestamp'], reverse=True)
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
                                key=f"history_radar_{idx}"
                            )
                        
                        if meal.get('has_allergens'):
                            st.error(f"⚠️ This meal contained allergens: {', '.join(meal['allergic_ingredients'])}")

        with tab3:
            st.header("Nutrition Statistics")
            if meal_history:
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(
                        viz_manager.create_meal_distribution(meal_history),
                        use_container_width=True,
                        key="stats_meal_dist"
                    )
                with col2:
                    st.plotly_chart(
                        viz_manager.create_allergen_exposure_chart(meal_history),
                        use_container_width=True,
                        key="stats_allergen"
                    )
                
                st.plotly_chart(
                    viz_manager.create_nutrition_timeline(meal_history),
                    use_container_width=True,
                    key="stats_timeline"
                )
                
                st.plotly_chart(
                    viz_manager.create_weekly_summary(meal_history,current_goal),
                    use_container_width=True,
                    key="stats_weekly"
                )

if __name__ == "__main__":
    main()