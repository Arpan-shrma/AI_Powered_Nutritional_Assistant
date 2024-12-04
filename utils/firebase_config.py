import firebase_admin
from firebase_admin import credentials, auth, firestore
import streamlit as st
from datetime import datetime, timezone
import pyrebase
import json
import os

class FirebaseConfig:
    _instance = None
    _initialized = False

    @staticmethod
    def get_instance():
        if FirebaseConfig._instance is None:
            FirebaseConfig._instance = FirebaseConfig()
        return FirebaseConfig._instance

    def __init__(self):
        if not FirebaseConfig._initialized:
            self.firebase = None
            self.pb_auth = None
            self.db = None
            self.initialize_firebase()
            FirebaseConfig._initialized = True

    def initialize_firebase(self):
        """Initialize both Firebase Admin SDK and Pyrebase"""
        try:
            # Initialize Firebase Admin SDK
            if not firebase_admin._apps:
                cred = credentials.Certificate('config/firebase_config.json')
                firebase_admin.initialize_app(cred)
            
            # Initialize Pyrebase
            with open('config/firebase_config.json', 'r') as f:
                config = json.load(f)

            firebase_config = {
                'apiKey': config.get('apiKey'),
                'authDomain': f"{config['project_id']}.firebaseapp.com",
                'projectId': config['project_id'],
                'storageBucket': f"{config['project_id']}.appspot.com",
                'messagingSenderId': config.get('messagingSenderId'),
                'appId': config.get('appId'),
                'databaseURL': '',
                'serviceAccount': 'config/firebase_config.json'
            }

            self.firebase = pyrebase.initialize_app(firebase_config)
            self.pb_auth = self.firebase.auth()
            self.db = firestore.client()
            
            return True
        except Exception as e:
            st.error(f"Firebase initialization error: {str(e)}")
            return False

class AuthManager:
    def __init__(self):
        firebase_config = FirebaseConfig.get_instance()
        self.pb_auth = firebase_config.pb_auth
        self.db = firebase_config.db

    def sign_up(self, email: str, password: str, name: str, height: float = None, weight: float = None) -> tuple:
        """
        Create new user account and profile
        Returns: (user_id, error_message)
        """
        try:
            # Create user with Pyrebase
            user = self.pb_auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            
            # Update user profile in Firebase Auth
            auth.update_user(
                uid,
                display_name=name,
                email_verified=False
            )
            
            # Create user profile in Firestore
            user_data = {
                'email': email,
                'name': name,
                'height': height,
                'weight': weight,
                'allergens': [],
                'dietary_preferences': [],
                'created_at': datetime.now(timezone.utc),
                'last_login': datetime.now(timezone.utc)
            }
            
            self.db.collection('users').document(uid).set(user_data)
            return uid, None
        
        except Exception as e:
            error_message = str(e)
            if "EMAIL_EXISTS" in error_message:
                return None, "Email already exists"
            return None, f"Sign up failed: {error_message}"

    def sign_in(self, email: str, password: str) -> tuple:
        """
        Sign in existing user
        Returns: (user_id, error_message)
        """
        try:
            # Sign in with Pyrebase
            user = self.pb_auth.sign_in_with_email_and_password(email, password)
            uid = user['localId']
            
            # Check if user document exists
            user_doc = self.db.collection('users').document(uid).get()
            
            if not user_doc.exists:
                # Create user profile if it doesn't exist
                user_data = {
                    'email': email,
                    'name': auth.get_user(uid).display_name or email.split('@')[0],
                    'height': None,
                    'weight': None,
                    'allergens': [],
                    'dietary_preferences': [],
                    'created_at': datetime.now(timezone.utc),
                    'last_login': datetime.now(timezone.utc)
                }
                self.db.collection('users').document(uid).set(user_data)
            else:
                # Update last login timestamp
                self.db.collection('users').document(uid).update({
                    'last_login': datetime.now(timezone.utc)
                })
            
            return uid, None
        
        except Exception as e:
            error_message = str(e)
            if "INVALID_PASSWORD" in error_message:
                return None, "Invalid password"
            elif "EMAIL_NOT_FOUND" in error_message:
                return None, "Email not found"
            return None, f"Sign in failed: {error_message}"

    def get_user_profile(self, user_id: str) -> dict:
        """Get user profile data"""
        try:
            doc = self.db.collection('users').document(user_id).get()
            return doc.to_dict() if doc.exists else None
        except Exception as e:
            st.error(f"Error fetching user profile: {str(e)}")
            return None

    def update_user_profile(self, user_id: str, update_data: dict) -> bool:
        """Update user profile"""
        try:
            update_data['updated_at'] = datetime.now(timezone.utc)
            self.db.collection('users').document(user_id).update(update_data)
            return True
        except Exception as e:
            st.error(f"Error updating profile: {str(e)}")
            return False

    def update_allergens(self, user_id: str, allergens: list) -> bool:
        """Update user allergens"""
        return self.update_user_profile(user_id, {'allergens': allergens})

    def update_dietary_preferences(self, user_id: str, preferences: list) -> bool:
        """Update user dietary preferences"""
        return self.update_user_profile(user_id, {'dietary_preferences': preferences})

    def reset_password(self, email: str) -> tuple:
        """Send password reset email"""
        try:
            self.pb_auth.send_password_reset_email(email)
            return True, None
        except Exception as e:
            return False, str(e)

    def delete_account(self, user_id: str) -> tuple:
        """Delete user account and all associated data"""
        try:
            # Delete user data from Firestore
            self.db.collection('users').document(user_id).delete()
            
            # Delete user authentication
            auth.delete_user(user_id)
            return True, None
        except Exception as e:
            return False, f"Error deleting account: {str(e)}"

    @staticmethod
    def init_session_state():
        """Initialize session state variables"""
        if 'user_id' not in st.session_state:
            st.session_state.user_id = None
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        if 'user_profile' not in st.session_state:
            st.session_state.user_profile = None