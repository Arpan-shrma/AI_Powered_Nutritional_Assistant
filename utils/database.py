import firebase_admin
from firebase_admin import firestore
import streamlit as st
from datetime import datetime, timezone
import json
from typing import Dict, List, Optional, Union
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.db = firestore.client()
        self._load_food_database()

    def _load_food_database(self):
        """Load food database without caching"""
        try:
            with open('data/food101_database.json', 'r') as f:
                self.food_db = json.load(f)
        except Exception as e:
            st.error(f"Error loading food database: {str(e)}")
            self.food_db = {}

    @staticmethod
    @st.cache_data
    def _cached_load_food_database() -> Dict:
        """Cached function to load food database"""
        try:
            with open('data/food101_database.json', 'r') as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading food database: {str(e)}")
            return {}

    def get_food_info(self, food_name: str) -> Optional[Dict]:
        """Get information about specific food"""
        # Use the cached database instead of instance variable
        food_db = self._cached_load_food_database()
        return food_db.get(food_name)

    def save_analysis(self, user_id: str, analysis_data: Dict) -> bool:
        """Save food analysis results"""
        try:
            analysis_data.update({
                'timestamp': datetime.now(timezone.utc),
                'shared': False
            })
            
            self.db.collection('users').document(user_id)\
                .collection('analyses').add(analysis_data)
            return True
        except Exception as e:
            st.error(f"Error saving analysis: {str(e)}")
            return False

    def get_user_analyses(self, user_id: str, limit: int = 10) -> List[Dict]:
        """Get user's food analyses history"""
        try:
            analyses = self.db.collection('users').document(user_id)\
                .collection('analyses')\
                .order_by('timestamp', direction='DESCENDING')\
                .limit(limit)\
                .stream()
            return [analysis.to_dict() for analysis in analyses]
        except Exception as e:
            st.error(f"Error fetching analyses: {str(e)}")
            return []

    def share_analysis(self, user_id: str, analysis_id: str) -> str:
        """Share analysis and get sharing link"""
        try:
            # Create shareable link
            share_data = {
                'user_id': user_id,
                'analysis_id': analysis_id,
                'shared_at': datetime.now(timezone.utc)
            }
            share_ref = self.db.collection('shared_analyses').add(share_data)
            
            # Update analysis as shared
            self.db.collection('users').document(user_id)\
                .collection('analyses').document(analysis_id)\
                .update({'shared': True})
            
            return share_ref[1].id  # Return sharing ID
        except Exception as e:
            st.error(f"Error sharing analysis: {str(e)}")
            return None

    def get_shared_analysis(self, share_id: str) -> Optional[Dict]:
        """Get shared analysis data"""
        try:
            share_doc = self.db.collection('shared_analyses').document(share_id).get()
            if not share_doc.exists:
                return None
            
            share_data = share_doc.to_dict()
            analysis_doc = self.db.collection('users').document(share_data['user_id'])\
                .collection('analyses').document(share_data['analysis_id']).get()
            
            return analysis_doc.to_dict() if analysis_doc.exists else None
        except Exception as e:
            st.error(f"Error fetching shared analysis: {str(e)}")
            return None

    def get_nutrition_stats(self, user_id: str) -> Dict:
        """Get user's nutrition statistics"""
        try:
            analyses = self.get_user_analyses(user_id, limit=100)  # Get last 100 analyses
            if not analyses:
                return {}
            
            df = pd.DataFrame(analyses)
            stats = {
                'total_meals': len(df),
                'avg_calories': df['calories'].mean() if 'calories' in df else 0,
                'avg_protein': df['protein'].mean() if 'protein' in df else 0,
                'common_foods': df['food_name'].value_counts().head(5).to_dict() if 'food_name' in df else {},
                'allergen_exposure': df['allergens'].explode().value_counts().to_dict() if 'allergens' in df else {}
            }
            return stats
        except Exception as e:
            st.error(f"Error calculating nutrition stats: {str(e)}")
            return {}

    def save_user_preferences(self, user_id: str, preferences: Dict) -> bool:
        """Save user dietary preferences"""
        try:
            self.db.collection('users').document(user_id)\
                .collection('preferences').document('dietary')\
                .set(preferences, merge=True)
            return True
        except Exception as e:
            st.error(f"Error saving preferences: {str(e)}")
            return False

    def get_user_preferences(self, user_id: str) -> Dict:
        """Get user dietary preferences"""
        try:
            doc = self.db.collection('users').document(user_id)\
                .collection('preferences').document('dietary').get()
            return doc.to_dict() if doc.exists else {}
        except Exception as e:
            st.error(f"Error fetching preferences: {str(e)}")
            return {}

    def export_user_data(self, user_id: str) -> Dict:
        """Export all user data"""
        try:
            user_doc = self.db.collection('users').document(user_id).get()
            analyses = self.get_user_analyses(user_id, limit=None)
            preferences = self.get_user_preferences(user_id)
            
            export_data = {
                'profile': user_doc.to_dict(),
                'analyses': analyses,
                'preferences': preferences,
                'exported_at': datetime.now(timezone.utc).isoformat()
            }
            return export_data
        except Exception as e:
            st.error(f"Error exporting user data: {str(e)}")
            return {}