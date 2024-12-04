import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import numpy as np

class VisualizationManager:
    def __init__(self):
        self.color_scheme = {
            'primary': '#FF4B4B',
            'secondary': '#0068C9',
            'tertiary': '#83C9FF',
            'success': '#29B09D',
            'warning': '#FFA421',
            'error': '#FF4B4B'
        }

    def create_daily_calorie_chart(self, meal_history, calorie_goal):
        """Create daily calorie tracking chart with better timestamp formatting"""
        df = pd.DataFrame(meal_history)
        df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
        df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
        
        daily_calories = df.groupby('date')['calories'].sum().reset_index()
        daily_calories['goal'] = calorie_goal
        
        fig = go.Figure()
        
        # Add calorie goal line
        fig.add_trace(go.Scatter(
            x=daily_calories['date'],
            y=daily_calories['goal'],
            name='Daily Goal',
            line=dict(color='rgba(255, 0, 0, 0.5)', dash='dash'),
            hovertemplate='Goal: %{y:.0f} kcal<br>Date: %{x}<extra></extra>'
        ))
        
        # Add daily calories bars
        fig.add_trace(go.Bar(
            x=daily_calories['date'],
            y=daily_calories['calories'],
            name='Calories Consumed',
            marker_color=np.where(
                daily_calories['calories'] <= daily_calories['goal'],
                self.color_scheme['success'],
                self.color_scheme['warning']
            ),
            hovertemplate='Consumed: %{y:.0f} kcal<br>Date: %{x}<extra></extra>'
        ))
        
        fig.update_layout(
            title='Daily Calorie Tracking',
            xaxis_title='Date',
            yaxis_title='Calories',
            hovermode='x unified',
            xaxis=dict(
                tickformat='%Y-%m-%d',
                tickmode='linear',
                dtick='D1',
                tickangle=45
            ),
            margin=dict(b=100)
        )
        
        return fig

    def create_nutrition_timeline(self, meal_history):
        """Create timeline of nutritional intake showing accumulating values throughout the day"""
        df = pd.DataFrame(meal_history)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Sort by timestamp to ensure proper accumulation
        df = df.sort_values('timestamp')
        
        # Calculate running totals for each day
        df['date'] = df['timestamp'].dt.date
        df['running_calories'] = df.groupby('date')['calories'].cumsum()
        df['running_protein'] = df.groupby('date')['protein'].cumsum()
        df['running_carbs'] = df.groupby('date')['carbs'].cumsum()
        df['running_fat'] = df.groupby('date')['fat'].cumsum()

        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Daily Calories', 'Daily Protein', 'Daily Carbs', 'Daily Fat')
        )

        # Add traces for running totals
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['running_calories'],
                mode='lines',
                name='Calories',
                line=dict(color=self.color_scheme['primary']),
                hovertemplate='Time: %{x|%H:%M}<br>Total Calories: %{y:.0f}<extra></extra>'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['running_protein'],
                mode='lines',
                name='Protein',
                line=dict(color=self.color_scheme['secondary']),
                hovertemplate='Time: %{x|%H:%M}<br>Total Protein: %{y:.1f}g<extra></extra>'
            ),
            row=1, col=2
        )
        
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['running_carbs'],
                mode='lines',
                name='Carbs',
                line=dict(color=self.color_scheme['tertiary']),
                hovertemplate='Time: %{x|%H:%M}<br>Total Carbs: %{y:.1f}g<extra></extra>'
            ),
            row=2, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['running_fat'],
                mode='lines',
                name='Fat',
                line=dict(color=self.color_scheme['success']),
                hovertemplate='Time: %{x|%H:%M}<br>Total Fat: %{y:.1f}g<extra></extra>'
            ),
            row=2, col=2
        )

        # Update layout for all x-axes
        for i in range(1, 3):
            for j in range(1, 3):
                fig.update_xaxes(
                    type='date',
                    tickformat='%H:%M',  # Show time format
                    dtick=3600000,  # Show hourly ticks (in milliseconds)
                    tickangle=45,
                    row=i, col=j
                )
                fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128, 128, 128, 0.2)', row=i, col=j)

        fig.update_layout(
            height=600,
            showlegend=False,
            margin=dict(b=100),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )

        # Update y-axis titles
        fig.update_yaxes(title_text="Calories", row=1, col=1)
        fig.update_yaxes(title_text="Protein (g)", row=1, col=2)
        fig.update_yaxes(title_text="Carbs (g)", row=2, col=1)
        fig.update_yaxes(title_text="Fat (g)", row=2, col=2)

        return fig

    def create_nutritional_radar(self, nutrition_data):
        """Create radar chart of nutritional values"""
        categories = ['Calories', 'Protein', 'Carbs', 'Fat', 'Fiber']
        if isinstance(nutrition_data, dict):
            values = [
                nutrition_data.get('calories', 0),
                nutrition_data.get('protein', 0),
                nutrition_data.get('carbs', 0),
                nutrition_data.get('fat', 0),
                nutrition_data.get('fiber', 0)
            ]
        else:
            values = [
                nutrition_data['calories'],
                nutrition_data['protein'],
                nutrition_data['carbs'],
                nutrition_data['fat'],
                nutrition_data['fiber']
            ]

        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            line=dict(color=self.color_scheme['secondary'])
        ))

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, max(values)])),
            showlegend=False
        )
        return fig

    def create_meal_distribution(self, meal_history):
        """Create pie chart of meal types"""
        df = pd.DataFrame(meal_history)
        meal_counts = df['food_name'].value_counts()

        fig = go.Figure(data=[go.Pie(
            labels=meal_counts.index,
            values=meal_counts.values,
            hole=.3,
            marker=dict(colors=px.colors.qualitative.Set3)
        )])
        
        fig.update_layout(
            title="Meal Types Distribution",
            showlegend=True
        )
        return fig

    def create_allergen_exposure_chart(self, meal_history):
        """Create enhanced bar chart of allergen exposure"""
        allergens = []
        for meal in meal_history:
            allergens.extend(meal.get('allergens', []))
        
        allergen_counts = pd.Series(allergens).value_counts()

        fig = go.Figure(data=[
            go.Bar(
                x=allergen_counts.index, 
                y=allergen_counts.values,
                marker_color=self.color_scheme['warning'],
                text=allergen_counts.values,
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title="Allergen Exposure Summary",
            xaxis_title="Allergen Type",
            yaxis_title="Number of Exposures",
            showlegend=False,
            hovermode='x'
        )
        return fig

    def create_weekly_summary(self, meal_history, calorie_goal):
        """Create weekly summary dashboard with daily format"""
        df = pd.DataFrame(meal_history)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date
        
        # Group by date
        daily_data = df.groupby('date').agg({
            'calories': 'sum',
            'protein': 'sum',
            'carbs': 'sum',
            'fat': 'sum'
        }).reset_index()
        
        # Get last 7 days
        week_ago = datetime.now().date() - timedelta(days=7)
        daily_data = daily_data[daily_data['date'] > week_ago]

        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{"type": "scatter"}, {"type": "bar"}],
                [{"colspan": 2}, {"type": "scatter"}]],
            subplot_titles=("Daily Calories vs Goal", "Nutrient Distribution", 
                        "Nutrient Trends"),
            row_heights=[0.5, 0.5]
        )

        # Daily calories vs goal
        fig.add_trace(
            go.Scatter(
                x=daily_data['date'],
                y=[calorie_goal] * len(daily_data),
                name='Goal',
                line=dict(color='blue', dash='dash'),
                hovertemplate='Goal: %{y:.0f} kcal<br>Date: %{x|%b %d}<extra></extra>'
            ),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(
                x=daily_data['date'],
                y=daily_data['calories'],
                mode='lines+markers',
                name='Actual',
                line=dict(color=self.color_scheme['primary']),
                hovertemplate='Consumed: %{y:.0f} kcal<br>Date: %{x|%b %d}<extra></extra>'
            ),
            row=1, col=1
        )

        # Nutrient distribution
        nutrients = ['protein', 'carbs', 'fat']
        avg_nutrients = [daily_data[nutrient].mean() for nutrient in nutrients]
        fig.add_trace(
            go.Bar(
                x=nutrients,
                y=avg_nutrients,
                marker_color=[self.color_scheme['secondary'], 
                            self.color_scheme['tertiary'], 
                            self.color_scheme['success']],
                text=[f'{val:.1f}g' for val in avg_nutrients],
                textposition='auto',
            ),
            row=1, col=2
        )

        # Nutrient trends
        for nutrient, color in zip(nutrients, [self.color_scheme['secondary'], 
                                            self.color_scheme['tertiary'], 
                                            self.color_scheme['success']]):
            fig.add_trace(
                go.Scatter(
                    x=daily_data['date'],
                    y=daily_data[nutrient],
                    mode='lines+markers',
                    name=nutrient.capitalize(),
                    line=dict(color=color),
                    hovertemplate='%{y:.1f}g<br>Date: %{x|%b %d}<extra></extra>'
                ),
                row=2, col=1
            )

        # Update x-axes formatting
        fig.update_xaxes(
            tickformat='%b %d',
            dtick='D1',
            tickangle=45,
            row=1, col=1
        )
        fig.update_xaxes(
            tickformat='%b %d',
            dtick='D1',
            tickangle=45,
            row=2, col=1
        )

        fig.update_layout(
            height=800,
            showlegend=True,
            margin=dict(b=100, t=100)
        )
        return fig
    def format_metrics(self, metrics_data):
        """Format metrics for streamlit metrics display"""
        return {
            'Calories': f"{metrics_data.get('calories', 0):.0f} kcal",
            'Protein': f"{metrics_data.get('protein', 0):.1f}g",
            'Carbs': f"{metrics_data.get('carbs', 0):.1f}g",
            'Fat': f"{metrics_data.get('fat', 0):.1f}g",
            'Fiber': f"{metrics_data.get('fiber', 0):.1f}g"
        }