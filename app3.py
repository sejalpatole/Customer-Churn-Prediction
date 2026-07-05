import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Customer Churn Prediction Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Load CSS
# ==========================================================

css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# Load ML Model
# ==========================================================

@st.cache_resource
def load_models():

    model = joblib.load("model.pkl")
    encoder = joblib.load("encoder.pkl")
    scaler = joblib.load("scaler.pkl")

    return model, encoder, scaler


model, encoder, scaler = load_models()

# ==========================================================
# Session State Defaults
# ==========================================================

defaults = {

    "gender": "Female",
    "senior_citizen": "No",
    "partner": "No",
    "dependents": "No",

    "tenure": 24,

    "phone_service": "Yes",
    "multiple_lines": "No",
    "internet_service": "DSL",

    "online_security": "No",
    "online_backup": "No",
    "device_protection": "No",

    "tech_support": "No",
    "streaming_tv": "No",
    "streaming_movies": "No",

    "contract": "Month-to-month",
    "paperless_billing": "Yes",

    "payment_method": "Electronic check",

    "monthly_charges": 70.0,
    "total_charges": 1680.0

}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown("## 🤖 Customer Churn Pro")

    st.markdown("---")

    page = st.radio(

        "Navigation",

        [

            "🏠 Dashboard",
            "👤 Customer Details",
            "🤖 Prediction",
            "📈 Analytics",
            "📄 Reports",
            "ℹ️ About"

        ]

    )

    st.markdown("---")

    st.success("✅ Random Forest Loaded")

    st.metric("Accuracy", "80%")
    st.metric("Dataset", "7032")
    st.metric("Features", "19")

    st.markdown("---")

    st.caption("Developed by Sejal Patole")

# ==========================================================
# Dashboard
# ==========================================================

if page == "🏠 Dashboard":

    st.title("📊 Customer Churn Prediction Pro")

    st.write(
        """
Welcome to the AI-powered Customer Churn Prediction System.

This application helps businesses:

- Predict customer churn
- Analyze customer behaviour
- Understand business insights
- Generate reports
"""
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🤖 Machine Learning Model")

    with col2:
        st.success("📊 Interactive Analytics")

    with col3:
        st.warning("📄 Business Reports")

# ==========================================================
# Placeholder Pages
# ==========================================================

elif page == "👤 Customer Details":

    st.title("👤 Customer Details")
    st.info("Part 2")

elif page == "🤖 Prediction":

    st.title("🤖 Prediction")
    st.info("Part 3")

elif page == "📈 Analytics":

    st.title("📈 Analytics")
    st.info("Part 4")

elif page == "📄 Reports":

    st.title("📄 Reports")
    st.info("Part 5")

else:

    st.title("ℹ️ About")

    st.write(
        """
Customer Churn Prediction Pro

Version 2.0

Developed by Sejal Patole
"""
    )