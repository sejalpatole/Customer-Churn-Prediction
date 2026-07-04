# ==========================================================
# Customer Churn Prediction Pro
# Main Application
# ==========================================================

import streamlit as st
import joblib

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
# Load ML Files
# ==========================================================

@st.cache_resource
def load_models():
    model = joblib.load("model.pkl")
    encoder = joblib.load("encoder.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, encoder, scaler

model, encoder, scaler = load_models()

# ==========================================================
# Session State
# ==========================================================

defaults = {

    "gender":"Female",
    "senior_citizen":"No",
    "partner":"No",
    "dependents":"No",

    "tenure":24,

    "phone_service":"Yes",
    "multiple_lines":"No",
    "internet_service":"DSL",

    "online_security":"No",
    "online_backup":"No",
    "device_protection":"No",

    "tech_support":"No",
    "streaming_tv":"No",
    "streaming_movies":"No",

    "contract":"Month-to-month",
    "paperless_billing":"Yes",

    "payment_method":"Electronic check",

    "monthly_charges":70.0,
    "total_charges":1680.0

}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================================
# Load CSS
# ==========================================================

with open("assets/style.css") as css:

    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    page = st.radio(

        "Navigation",

        [

            "🏠 Dashboard",

            "👤 Customer Details",

            "🤖 Prediction",

            "📈 Analytics",

            "📄 Reports",

            "ℹ About"

        ]

    )

    st.markdown("---")

    st.success("✅ Random Forest Model Loaded")

    st.metric("Accuracy","80%")

    st.metric("Dataset","7032")

    st.metric("Features","19")

    st.markdown("---")

    st.caption("Developed by Sejal Patole")

# ==========================================================
# Dashboard
# ==========================================================

if page=="🏠 Dashboard":

    st.markdown("""

<div class="hero">

<h1>📊 Customer Churn Prediction Pro</h1>

<p>

AI-powered customer retention system built using

Machine Learning and Streamlit.

Predict customer churn,

analyze risk,

and generate business insights instantly.

</p>

</div>

""",unsafe_allow_html=True)

    st.write("")

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.markdown("""

<div class="card">

<h2>🤖</h2>

<h3>Random Forest</h3>

<p>ML Model</p>

</div>

""",unsafe_allow_html=True)

    with c2:

        st.markdown("""

<div class="card">

<h2>🎯</h2>

<h3>80%</h3>

<p>Accuracy</p>

</div>

""",unsafe_allow_html=True)

    with c3:

        st.markdown("""

<div class="card">

<h2>👥</h2>

<h3>7032</h3>

<p>Customers</p>

</div>

""",unsafe_allow_html=True)

    with c4:

        st.markdown("""

<div class="card">

<h2>📋</h2>

<h3>19</h3>

<p>Features</p>

</div>

""",unsafe_allow_html=True)

    st.write("")

    left,right=st.columns([2,1])

    with left:

        st.subheader("🚀 Welcome")

        st.info("""

This dashboard helps telecom companies identify customers who are likely to leave.

Workflow

• Enter Customer Details

• Run AI Prediction

• Analyze Customer Risk

• View Business Insights

• Download Report

""")

    with right:

        st.subheader("✨ Features")

        st.success("AI Prediction")

        st.success("Risk Analysis")

        st.success("Interactive Charts")

        st.success("Executive Summary")

        st.success("CSV Reports")

# ==========================================================
# Customer Page
# ==========================================================

elif page=="👤 Customer Details":

    st.info("Customer Details page will be added in Part 2.")

# ==========================================================
# Prediction Page
# ==========================================================

elif page=="🤖 Prediction":

    st.info("Prediction page will be added in Part 3.")

# ==========================================================
# Analytics Page
# ==========================================================

elif page=="📈 Analytics":

    st.info("Analytics page will be added in Part 4.")

# ==========================================================
# Reports Page
# ==========================================================

elif page=="📄 Reports":

    st.info("Reports page will be added in Part 5.")

# ==========================================================
# About
# ==========================================================

else:

    st.title("ℹ About")

    st.write("""

Customer Churn Prediction Pro

Built using

• Streamlit

• Scikit-learn

• Plotly

• Pandas

Developed by Sejal Patole

""")