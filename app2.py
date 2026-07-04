# ==========================================================
# CUSTOMER CHURN PREDICTION PRO
# Part 1 : Imports, Configuration & Hero Section
# Developed by Sejal Patole
# ==========================================================

import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Load ML Model
# ----------------------------------------------------------

model = joblib.load("model.pkl")
label_encoders = joblib.load("encoder.pkl")
scaler = joblib.load("scaler.pkl")

# ----------------------------------------------------------
# Custom CSS
# ----------------------------------------------------------

st.markdown("""
<style>

/* Hide Streamlit Branding */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Main Background */

.stApp{
background:linear-gradient(to right,#eef2ff,#ffffff);
}

/* Hero Title */

.hero-title{
font-size:48px;
font-weight:800;
color:#1e3a8a;
text-align:center;
margin-top:10px;
margin-bottom:10px;
}

/* Hero Subtitle */

.hero-subtitle{
font-size:20px;
text-align:center;
color:#6b7280;
margin-bottom:35px;
}

/* KPI Cards */

.metric-card{
background:white;
padding:22px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,0.08);
text-align:center;
transition:0.3s;
}

.metric-card:hover{
transform:translateY(-6px);
box-shadow:0px 12px 25px rgba(0,0,0,0.15);
}

/* Section Header */

.section-title{
font-size:30px;
font-weight:bold;
color:#1e3a8a;
margin-top:25px;
margin-bottom:20px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:#1E3A8A;
}

section[data-testid="stSidebar"] *{
color:white;
}

/* Predict Button */

.stButton>button{
background:#2563eb;
color:white;
font-size:18px;
font-weight:bold;
border-radius:12px;
padding:14px;
width:100%;
border:none;
}

.stButton>button:hover{
background:#1d4ed8;
}

/* Footer */

.footer{
text-align:center;
padding:20px;
color:gray;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Hero Section
# ----------------------------------------------------------

st.markdown("""
<div class="hero-title">
📊 Customer Churn Prediction Pro
</div>

<div class="hero-subtitle">
Predict whether a telecom customer is likely to leave using Machine Learning
and receive AI-powered business recommendations.
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# KPI Cards
# ----------------------------------------------------------

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
        <h4>👥 Dataset</h4>
        <h2>7032</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.success("✅ Model Loaded Successfully")

    st.info("""
This application predicts whether a telecom customer is likely to churn.

Simply enter the customer information and click **Predict** to receive:

• Churn Prediction

• Risk Score

• AI Business Insights

• Retention Strategy
""")

    st.markdown("---")

    st.subheader("📌 Workflow")

    st.write("1️⃣ Enter Customer Details")

    st.write("2️⃣ Click Predict")

    st.write("3️⃣ View AI Analysis")

    st.write("4️⃣ Download Report")

    st.markdown("---")

    st.caption("Developed by Sejal Patole")

# ==========================================================
# PART 2 : Customer Information
# ==========================================================

st.markdown(
    """
    <div class="section-title">
        👤 Customer Information
    </div>
    """,
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        senior_citizen = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

        partner = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

    with col2:

        dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

        tenure = st.slider(
            "Tenure (Months)",
            0,
            72,
            24
        )

st.markdown("---")


# ==========================================================
# PART 2 : Services
# ==========================================================

st.markdown(
    """
    <div class="section-title">
        📞 Telecom Services
    </div>
    """,
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2, col3 = st.columns(3)

    with col1:

        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            [
                "No",
                "Yes",
                "No phone service"
            ]
        )

        internet_service = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

    with col2:

        online_security = st.selectbox(
            "Online Security",
            [
                "No",
                "Yes",
                "No internet service"
            ]
        )

        online_backup = st.selectbox(
            "Online Backup",
            [
                "No",
                "Yes",
                "No internet service"
            ]
        )

        device_protection = st.selectbox(
            "Device Protection",
            [
                "No",
                "Yes",
                "No internet service"
            ]
        )

    with col3:

        tech_support = st.selectbox(
            "Tech Support",
            [
                "No",
                "Yes",
                "No internet service"
            ]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            [
                "No",
                "Yes",
                "No internet service"
            ]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            [
                "No",
                "Yes",
                "No internet service"
            ]
        )

st.markdown("---")


# ==========================================================
# PART 2 : Billing & Contract Details
# ==========================================================

st.markdown(
    """
    <div class="section-title">
        💳 Billing & Contract
    </div>
    """,
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

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

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    with col2:

        monthly_charges = st.slider(
            "Monthly Charges ($)",
            18.0,
            120.0,
            70.0,
            step=0.5
        )

        total_charges = st.number_input(
            "Total Charges ($)",
            min_value=0.0,
            value=float(round(monthly_charges * tenure, 2)),
            step=1.0
        )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# PART 3 : AI Prediction
# ==========================================================

st.markdown(
    """
    <div class="section-title">
        🤖 AI Customer Churn Analysis
    </div>
    """,
    unsafe_allow_html=True
)

predict = st.button(
    "🚀 Predict Customer Churn",
    use_container_width=True
)

if predict:

    # -----------------------------
    # Create Input DataFrame
    # -----------------------------

    input_df = pd.DataFrame({

        "gender":[gender],
        "SeniorCitizen":[1 if senior_citizen=="Yes" else 0],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[phone_service],
        "MultipleLines":[multiple_lines],
        "InternetService":[internet_service],
        "OnlineSecurity":[online_security],
        "OnlineBackup":[online_backup],
        "DeviceProtection":[device_protection],
        "TechSupport":[tech_support],
        "StreamingTV":[streaming_tv],
        "StreamingMovies":[streaming_movies],
        "Contract":[contract],
        "PaperlessBilling":[paperless_billing],
        "PaymentMethod":[payment_method],
        "MonthlyCharges":[monthly_charges],
        "TotalCharges":[total_charges]

    })

    # -----------------------------
    # Encode Categorical Features
    # -----------------------------

    categorical_cols = input_df.select_dtypes(include="object").columns

    for col in categorical_cols:
        input_df[col] = label_encoders[col].transform(input_df[col])

    # -----------------------------
    # Scale Numerical Features
    # -----------------------------

    numerical_cols = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    input_df[numerical_cols] = scaler.transform(
        input_df[numerical_cols]
    )

    # -----------------------------
    # Prediction
    # -----------------------------

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    churn_probability = probability[1] * 100

    confidence = max(probability) * 100

    # -----------------------------
    # Result
    # -----------------------------

    st.markdown("---")

    left, right = st.columns([1,2])

    with left:

        if prediction == 1:

            st.error("## 🔴 High Churn Risk")

            risk = "HIGH"

        else:

            st.success("## 🟢 Low Churn Risk")

            risk = "LOW"

        st.metric(
            "🎯 AI Confidence",
            f"{confidence:.2f}%"
        )

        st.metric(
            "📉 Churn Probability",
            f"{churn_probability:.2f}%"
        )

        st.progress(churn_probability/100)

    with right:

        st.info(f"""

### 📊 Prediction Summary

**Prediction :**
{"Customer Likely to Churn" if prediction==1 else "Customer Likely to Stay"}

**Risk Level :**
{risk}

**AI Confidence :**
{confidence:.2f}%

**Churn Probability :**
{churn_probability:.2f}%

""")

        if prediction == 1:

            st.warning("""

### ⚠️ Immediate Retention Strategy

✅ Contact customer immediately

✅ Offer loyalty discount

✅ Recommend yearly contract

✅ Improve customer support

✅ Provide personalized offers

""")

        else:

            st.success("""

### 🎉 Customer Retention Strategy

✅ Reward customer loyalty

✅ Recommend premium services

✅ Continue quality support

✅ Send appreciation emails

✅ Keep regular engagement

""")
            
    st.markdown("---")

    st.markdown(
        """
        <div class="section-title">
            📊 AI Analytics Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # Gauge Chart
    # =====================================================

    gauge = go.Figure(go.Indicator(

        mode="gauge+number",

        value=churn_probability,

        number={
            'suffix':"%",
            'font':{'size':40}
        },

        title={
            'text':"Customer Churn Risk",
            'font':{'size':24}
        },

        gauge={

            'axis':{'range':[0,100]},

            'bar':{'color':"#2563EB"},

            'steps':[

                {'range':[0,35],'color':"#DCFCE7"},
                {'range':[35,70],'color':"#FEF3C7"},
                {'range':[70,100],'color':"#FECACA"}

            ]

        }

    ))

    gauge.update_layout(height=350)

    # =====================================================
    # Probability Pie Chart
    # =====================================================

    pie = px.pie(

        values=[
            100-churn_probability,
            churn_probability
        ],

        names=[
            "Stay",
            "Churn"
        ],

        hole=0.55,

        title="Prediction Probability"

    )

    pie.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    # =====================================================
    # Display Charts
    # =====================================================

    chart1, chart2 = st.columns(2)

    with chart1:
        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with chart2:
        st.plotly_chart(
            pie,
            use_container_width=True
        )

    st.markdown("---")

    # =====================================================
    # Customer Health Score
    # =====================================================

    health_score = round(100 - churn_probability)

    st.subheader("💚 Customer Health Score")

    score_col1, score_col2 = st.columns([1,3])

    with score_col1:

        if health_score >= 75:
            st.success(f"# {health_score}/100")

        elif health_score >= 50:
            st.warning(f"# {health_score}/100")

        else:
            st.error(f"# {health_score}/100")

    with score_col2:

        st.progress(health_score/100)

        if health_score >= 75:

            st.success(
                "Customer relationship appears healthy with a low likelihood of churn."
            )

        elif health_score >= 50:

            st.warning(
                "Customer shows moderate churn risk. Consider proactive engagement."
            )

        else:

            st.error(
                "Customer is at high risk of churning. Immediate retention action is recommended."
            )

    st.markdown("---")

    # =====================================================
    # AI Insights
    # =====================================================

    st.subheader("🤖 AI Business Insights")

    insights = []

    if contract == "Month-to-month":
        insights.append(
            "• Month-to-month contracts generally have higher churn risk."
        )

    if monthly_charges > 80:
        insights.append(
            "• High monthly charges may increase customer dissatisfaction."
        )

    if tenure < 12:
        insights.append(
            "• Newer customers are generally more likely to churn."
        )

    if online_security == "No":
        insights.append(
            "• Customers without Online Security often churn more frequently."
        )

    if tech_support == "No":
        insights.append(
            "• Lack of Tech Support is a strong churn indicator."
        )

    if payment_method == "Electronic check":
        insights.append(
            "• Electronic Check customers historically show higher churn rates."
        )

    if len(insights) == 0:

        st.success(
            "✅ No major churn indicators detected. Customer profile looks stable."
        )

    else:

        for item in insights:
            st.write(item)

    # ==========================================================
# PART 4 : Advanced AI Analytics
# ==========================================================

st.markdown("---")

st.markdown("""
<div class="section-title">
📈 Advanced Customer Analytics
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Customer Health Score
# ----------------------------------------------------------

health_score = round(100 - churn_probability)

risk_score = round(churn_probability)

k1, k2, k3 = st.columns(3)

with k1:
    st.metric(
        "💚 Health Score",
        f"{health_score}/100"
    )

with k2:
    st.metric(
        "⚠ Risk Score",
        f"{risk_score}/100"
    )

with k3:
    if prediction == 1:
        st.metric(
            "Status",
            "High Risk 🔴"
        )
    else:
        st.metric(
            "Status",
            "Low Risk 🟢"
        )

st.markdown("---")

# ----------------------------------------------------------
# Feature Importance (Business Rules)
# ----------------------------------------------------------

importance = {}

importance["Monthly Charges"] = min(monthly_charges,100)

importance["Tenure"] = 100-(tenure/72*100)

importance["Contract"] = 95 if contract=="Month-to-month" else 40

importance["Tech Support"] = 90 if tech_support=="No" else 20

importance["Online Security"] = 85 if online_security=="No" else 25

importance["Payment Method"] = 80 if payment_method=="Electronic check" else 30

feature_df = pd.DataFrame({

    "Feature":importance.keys(),

    "Impact":importance.values()

})

feature_df = feature_df.sort_values(
    by="Impact",
    ascending=True
)

fig = px.bar(

    feature_df,

    x="Impact",

    y="Feature",

    orientation="h",

    text="Impact",

    title="Estimated Feature Impact"

)

fig.update_layout(
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------------------------------
# Probability Comparison
# ----------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    stay = 100-churn_probability

    st.metric(
        "Customer Staying",
        f"{stay:.2f}%"
    )

    st.progress(stay/100)

with col2:

    st.metric(
        "Customer Churning",
        f"{churn_probability:.2f}%"
    )

    st.progress(churn_probability/100)

st.markdown("---")

# ----------------------------------------------------------
# Executive Summary
# ----------------------------------------------------------

st.subheader("📋 Executive Summary")

summary = []

if prediction == 1:

    summary.append(
        "Customer is likely to churn."
    )

else:

    summary.append(
        "Customer is likely to stay."
    )

if tenure < 12:
    summary.append(
        "Customer has relatively low tenure."
    )

if monthly_charges > 80:
    summary.append(
        "Monthly charges are comparatively high."
    )

if contract=="Month-to-month":
    summary.append(
        "Month-to-month contracts generally have higher churn."
    )

if online_security=="No":
    summary.append(
        "Customer is not subscribed to Online Security."
    )

if tech_support=="No":
    summary.append(
        "Tech Support service is unavailable."
    )

for point in summary:
    st.write("✅", point)

    # ==========================================================
# PART 5 : Export Report & Final Dashboard
# ==========================================================

st.markdown("---")

st.markdown("""
<div class="section-title">
📄 Prediction Report
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Create Report
# ----------------------------------------------------------

report = pd.DataFrame({

    "Parameter":[

        "Prediction",
        "Risk Level",
        "AI Confidence (%)",
        "Churn Probability (%)",
        "Health Score",
        "Gender",
        "Tenure",
        "Contract",
        "Monthly Charges",
        "Payment Method"

    ],

    "Value":[

        "Likely to Churn" if prediction==1 else "Likely to Stay",

        risk,

        round(confidence,2),

        round(churn_probability,2),

        health_score,

        gender,

        tenure,

        contract,

        monthly_charges,

        payment_method

    ]

})

st.dataframe(
    report,
    use_container_width=True,
    hide_index=True
)

csv = report.to_csv(index=False).encode("utf-8")

st.download_button(

    "📥 Download Prediction Report",

    csv,

    file_name="customer_churn_prediction_report.csv",

    mime="text/csv",

    use_container_width=True

)

st.markdown("---")

# ==========================================================
# Prediction History (Current Session)
# ==========================================================

if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append({

    "Prediction":"Churn" if prediction==1 else "Stay",

    "Probability":round(churn_probability,2),

    "Confidence":round(confidence,2),

    "Risk":risk

})

history_df = pd.DataFrame(st.session_state.history)

st.subheader("🕒 Prediction History")

st.dataframe(

    history_df,

    use_container_width=True,

    hide_index=True

)

# ==========================================================
# Dashboard Statistics
# ==========================================================

st.markdown("---")

st.subheader("📊 Dashboard Statistics")

s1, s2, s3 = st.columns(3)

with s1:
    st.metric(
        "Predictions Made",
        len(history_df)
    )

with s2:
    st.metric(
        "Average Confidence",
        f"{history_df['Confidence'].mean():.2f}%"
    )

with s3:
    st.metric(
        "Average Churn Probability",
        f"{history_df['Probability'].mean():.2f}%"
    )

# ==========================================================
# Thank You Card
# ==========================================================

st.markdown("---")

st.success("""

## 🎉 Analysis Complete!

Thank you for using **Customer Churn Prediction Pro**.

The AI model has successfully analyzed the customer's profile and generated:

✅ Churn Prediction

✅ Confidence Score

✅ Customer Health Score

✅ Risk Analysis

✅ Business Insights

✅ Executive Summary

✅ Downloadable Report

""")

# ==========================================================
# Footer
# ==========================================================

st.markdown("""

<br><br>

<hr>

<div style='text-align:center;color:gray;'>

<h4>🤖 Customer Churn Prediction Pro</h4>

Machine Learning Project using Streamlit • Scikit-learn • Plotly

<br>

Developed by <b>Sejal Patole</b>

</div>

""", unsafe_allow_html=True)