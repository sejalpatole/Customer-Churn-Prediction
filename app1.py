# ==========================================
# Customer Churn Prediction Dashboard
# ==========================================

# Import Libraries
import streamlit as st
import pandas as pd
import joblib

# ------------------------------------------
# Load Model & Preprocessing Objects
# ------------------------------------------
model = joblib.load("model.pkl")
label_encoders = joblib.load("encoder.pkl")
scaler = joblib.load("scaler.pkl")

# ------------------------------------------
# Page Configuration
# ------------------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------
# Custom CSS
# ------------------------------------------
st.markdown("""
<style>

/* Main background */
.main{
    background:#F4F7FC;
}

/* Hide Streamlit menu & footer */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Dashboard Title */
.dashboard-title{
    font-size:42px;
    font-weight:700;
    color:#1E3A8A;
    text-align:center;
}

.dashboard-subtitle{
    text-align:center;
    color:#6B7280;
    font-size:18px;
    margin-bottom:30px;
}

/* KPI Cards */
.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    text-align:center;
}

/* Section Heading */
.section-title{
    font-size:24px;
    font-weight:600;
    color:#1E3A8A;
    margin-top:25px;
    margin-bottom:10px;
}

hr{
    border:none;
    height:1px;
    background:#E5E7EB;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# Dashboard Header
# ------------------------------------------
st.markdown("""
<div class="dashboard-title">
📊 Customer Churn Prediction Dashboard
</div>

<div class="dashboard-subtitle">
Predict customer churn using Machine Learning and gain actionable business insights.
</div>
""", unsafe_allow_html=True)

# ------------------------------------------
# KPI Cards
# ------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
    <h4>🤖 Model</h4>
    <h2>Random Forest</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
    <h4>🎯 Accuracy</h4>
    <h2>80%</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
    <h4>📋 Features</h4>
    <h2>19</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
    <h4>👥 Customers</h4>
    <h2>7032</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)

    st.title("Dashboard")

    st.markdown("---")

    st.success("✔ Model Loaded")

    st.info("""
This dashboard predicts whether a telecom customer is likely to churn using a Machine Learning model.
""")

    st.markdown("---")

    st.markdown("### 📌 Workflow")

    st.write("① Enter Customer Details")
    st.write("② Click Predict")
    st.write("③ View Prediction")
    st.write("④ Business Recommendation")

    st.markdown("---")

    st.caption("Developed by Sejal Patole")

# ==========================================
# Customer Profile Section
# ==========================================

st.markdown("""
<div class='section-title'>
👤 Customer Profile
</div>
""", unsafe_allow_html=True)

profile_col1, profile_col2 = st.columns(2)

with profile_col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

with profile_col2:

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# Internet & Services
# ==========================================

st.markdown("""
<div class='section-title'>
📞 Internet & Services
</div>
""", unsafe_allow_html=True)

service_col1, service_col2, service_col3 = st.columns(3)

# ------------------------------------------
# Column 1
# ------------------------------------------

with service_col1:

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

# ------------------------------------------
# Column 2
# ------------------------------------------

with service_col2:

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

# ------------------------------------------
# Column 3
# ------------------------------------------

with service_col3:

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# Billing & Contract Information
# ==========================================

st.markdown("""
<div class='section-title'>
💳 Billing & Contract Information
</div>
""", unsafe_allow_html=True)

bill_col1, bill_col2 = st.columns(2)

# ------------------------------------------
# Left Column
# ------------------------------------------

with bill_col1:

    tenure = st.slider(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=24,
        help="Number of months the customer has stayed with the company."
    )

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.radio(
        "Paperless Billing",
        ["Yes", "No"],
        horizontal=True
    )

# ------------------------------------------
# Right Column
# ------------------------------------------

with bill_col2:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.slider(
        "Monthly Charges ($)",
        min_value=18.0,
        max_value=120.0,
        value=70.0,
        step=0.5
    )

    total_charges = st.number_input(
        "Total Charges ($)",
        min_value=0.0,
        value=float(round(monthly_charges * tenure, 2)),
        step=1.0,
        help="Modify this value if necessary."
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# Prediction Dashboard
# ==========================================

st.markdown("""
<div class='section-title'>
🔮 Customer Churn Prediction
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Predict Customer Churn", use_container_width=True):

    # Create input dataframe
    input_df = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [1 if senior_citizen == "Yes" else 0],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    # Encode categorical values
    categorical_cols = input_df.select_dtypes(include="object").columns

    for col in categorical_cols:
        input_df[col] = label_encoders[col].transform(input_df[col])

    # Scale numerical columns
    numerical_cols = ["tenure", "MonthlyCharges", "TotalCharges"]

    input_df[numerical_cols] = scaler.transform(
        input_df[numerical_cols]
    )

    # Predict
    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    confidence = max(probability) * 100

    churn_probability = probability[1] * 100

    st.markdown("---")

    result_col1, result_col2 = st.columns([1, 2])

    with result_col1:

        if prediction == 1:
            st.error("## ⚠️ High Churn Risk")
        else:
            st.success("## ✅ Low Churn Risk")

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )

        st.progress(churn_probability / 100)

    with result_col2:

        st.subheader("📋 Business Recommendation")

        if prediction == 1:

            st.warning("""
### Immediate Actions

✅ Contact the customer

✅ Offer loyalty discounts

✅ Upgrade to annual plan

✅ Provide personalized offers

✅ Improve customer support

✅ Schedule a follow-up call
""")

        else:

            st.success("""
### Retention Strategy

✅ Reward loyal customers

✅ Offer premium services

✅ Send appreciation emails

✅ Continue quality support

✅ Recommend additional services

✅ Keep regular engagement
""")