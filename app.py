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

    st.markdown("""
    <div style="padding:30px;
                border-radius:20px;
                background:linear-gradient(135deg,#2563eb,#7c3aed);
                color:white;">
        <h1>📊 Customer Churn Prediction Pro</h1>
        <h4>AI-Powered Customer Retention Dashboard</h4>
        <p>
        Predict customer churn, analyze customer behaviour,
        and generate business insights using Machine Learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # KPI Cards

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🤖 Model",
            "Random Forest"
        )

    with c2:
        st.metric(
            "🎯 Accuracy",
            "80%"
        )

    with c3:
        st.metric(
            "👥 Customers",
            "7032"
        )

    with c4:
        st.metric(
            "📋 Features",
            "19"
        )

    st.divider()

    left, right = st.columns([2,1])

    with left:

        st.subheader("🚀 Project Overview")

        st.info("""

### Customer Churn Prediction Pro

This AI application helps telecom companies identify
customers who are likely to leave.

### Workflow

✅ Enter Customer Details

✅ Run AI Prediction

✅ Analyze Risk

✅ View Analytics Dashboard

✅ Generate Business Reports

""")

    with right:

        st.subheader("✨ Key Features")

        st.success("Machine Learning")

        st.success("Risk Analysis")

        st.success("Interactive Charts")

        st.success("Business Insights")

        st.success("Download Reports")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📈 Why Predict Churn?")

        st.write("""

- Reduce customer loss

- Increase retention

- Improve revenue

- Target high-risk customers

- Better business decisions

""")

    with col2:

        st.subheader("🧠 AI Model")

        st.write("""

**Algorithm**

Random Forest Classifier

**Dataset**

7032 Telecom Customers

**Input Features**

19

**Output**

Customer Will Churn / Stay

""")

    st.divider()

    st.success(
        "🎉 Ready to predict customer churn! Use the navigation menu on the left to begin."
    )

# ==========================================================
# Placeholder Pages
# ==========================================================

# ==========================================================
# Customer Details
# ==========================================================

elif page == "👤 Customer Details":

    st.title("👤 Customer Information")

    st.caption("Fill in the customer details required for churn prediction.")

    st.divider()

    # ==================================================
    # Personal Information
    # ==================================================

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        st.session_state.gender = st.selectbox(
            "Gender",
            ["Female", "Male"],
            index=["Female", "Male"].index(st.session_state.gender)
        )

        st.session_state.senior_citizen = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"],
            index=["No", "Yes"].index(st.session_state.senior_citizen)
        )

        st.session_state.partner = st.selectbox(
            "Partner",
            ["No", "Yes"],
            index=["No", "Yes"].index(st.session_state.partner)
        )

    with col2:

        st.session_state.dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"],
            index=["No", "Yes"].index(st.session_state.dependents)
        )

        st.session_state.tenure = st.slider(
            "Customer Tenure (Months)",
            0,
            72,
            st.session_state.tenure
        )

    st.divider()

    # ==================================================
    # Telecom Services
    # ==================================================

    st.subheader("📡 Telecom Services")

    col1, col2 = st.columns(2)

    with col1:

        st.session_state.phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"],
            index=["Yes", "No"].index(st.session_state.phone_service)
        )

        st.session_state.multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes", "No phone service"],
            index=["No", "Yes", "No phone service"].index(st.session_state.multiple_lines)
        )

        st.session_state.internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"],
            index=["DSL", "Fiber optic", "No"].index(st.session_state.internet_service)
        )

        st.session_state.online_security = st.selectbox(
            "Online Security",
            ["No", "Yes", "No internet service"],
            index=["No", "Yes", "No internet service"].index(st.session_state.online_security)
        )

    with col2:

        st.session_state.online_backup = st.selectbox(
            "Online Backup",
            ["No", "Yes", "No internet service"],
            index=["No", "Yes", "No internet service"].index(st.session_state.online_backup)
        )

        st.session_state.device_protection = st.selectbox(
            "Device Protection",
            ["No", "Yes", "No internet service"],
            index=["No", "Yes", "No internet service"].index(st.session_state.device_protection)
        )

        st.session_state.tech_support = st.selectbox(
            "Tech Support",
            ["No", "Yes", "No internet service"],
            index=["No", "Yes", "No internet service"].index(st.session_state.tech_support)
        )

        st.session_state.streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"],
            index=["No", "Yes", "No internet service"].index(st.session_state.streaming_tv)
        )

    st.session_state.streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"],
        index=["No", "Yes", "No internet service"].index(st.session_state.streaming_movies)
    )

    st.divider()

    # ==================================================
    # Billing Information
    # ==================================================

    st.subheader("💳 Billing Information")

    col1, col2 = st.columns(2)

    with col1:

        st.session_state.contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"],
            index=["Month-to-month", "One year", "Two year"].index(st.session_state.contract)
        )

        st.session_state.paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"],
            index=["Yes", "No"].index(st.session_state.paperless_billing)
        )

    with col2:

        st.session_state.payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ],
            index=[
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ].index(st.session_state.payment_method)
        )

        st.session_state.monthly_charges = st.number_input(
            "Monthly Charges ($)",
            0.0,
            1000.0,
            float(st.session_state.monthly_charges)
        )

        st.session_state.total_charges = st.number_input(
            "Total Charges ($)",
            0.0,
            100000.0,
            float(st.session_state.total_charges)
        )

    st.divider()

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        if st.button(
            "💾 Save Customer Information",
            use_container_width=True
        ):

            st.success("✅ Customer information saved successfully!")

            st.balloons()

# ==========================================================
# AI Prediction
# ==========================================================

elif page == "🤖 Prediction":

    st.title("🤖 AI Customer Churn Prediction")

    st.write(
        "Click the button below to predict whether the customer is likely to churn."
    )

    st.divider()

    if st.button("🚀 Predict Customer Churn", use_container_width=True):

        import pandas as pd

        # ---------------------------------
        # Create Input DataFrame
        # ---------------------------------

        input_data = pd.DataFrame([{

            "gender": st.session_state.gender,
            "SeniorCitizen": 1 if st.session_state.senior_citizen == "Yes" else 0,
            "Partner": st.session_state.partner,
            "Dependents": st.session_state.dependents,
            "tenure": st.session_state.tenure,
            "PhoneService": st.session_state.phone_service,
            "MultipleLines": st.session_state.multiple_lines,
            "InternetService": st.session_state.internet_service,
            "OnlineSecurity": st.session_state.online_security,
            "OnlineBackup": st.session_state.online_backup,
            "DeviceProtection": st.session_state.device_protection,
            "TechSupport": st.session_state.tech_support,
            "StreamingTV": st.session_state.streaming_tv,
            "StreamingMovies": st.session_state.streaming_movies,
            "Contract": st.session_state.contract,
            "PaperlessBilling": st.session_state.paperless_billing,
            "PaymentMethod": st.session_state.payment_method,
            "MonthlyCharges": st.session_state.monthly_charges,
            "TotalCharges": st.session_state.total_charges

        }])

        # ---------------------------------
        # Encode Categorical Columns
        # ---------------------------------

        categorical_columns = input_data.select_dtypes(include="object").columns

        for col in categorical_columns:

            if col in encoder:

                input_data[col] = encoder[col].transform(input_data[col])

        # ---------------------------------
        # Scale Features
        # ---------------------------------

        st.write("Input Columns")
        st.write(input_data.columns.tolist())

        st.write("Scaler expects")
        st.write(list(scaler.feature_names_in_))

        st.stop()
        input_scaled = scaler.transform(input_data)

        # ---------------------------------
        # Predict
        # ---------------------------------

        prediction = model.predict(input_scaled)[0]

        probability = model.predict_proba(input_scaled)[0][1]

        st.divider()

        st.subheader("📊 Prediction Result")

        if prediction == 1:

            st.error("🚨 High Churn Risk")

        else:

            st.success("✅ Customer Likely to Stay")

        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

        st.progress(float(probability))

        st.divider()

        # ---------------------------------
        # Risk Level
        # ---------------------------------

        if probability < 0.30:

            st.success("🟢 Low Risk")

        elif probability < 0.70:

            st.warning("🟡 Medium Risk")

        else:

            st.error("🔴 High Risk")

        st.divider()

        # ---------------------------------
        # Customer Summary
        # ---------------------------------

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Tenure",
                f"{st.session_state.tenure} Months"
            )

        with c2:

            st.metric(
                "Monthly Charges",
                f"${st.session_state.monthly_charges:.2f}"
            )

        with c3:

            st.metric(
                "Contract",
                st.session_state.contract
            )

        st.divider()

        st.subheader("💡 AI Recommendation")

        if probability < 0.30:

            st.success("""

Customer is highly satisfied.

Recommended Actions

✅ Continue loyalty program

✅ Offer premium upgrades

✅ Maintain service quality

""")

        elif probability < 0.70:

            st.warning("""

Customer shows moderate churn risk.

Recommended Actions

• Offer personalized discounts

• Improve engagement

• Promote value-added services

""")

        else:

            st.error("""

Customer is at HIGH risk of churn.

Immediate Action Recommended

• Contact customer immediately

• Offer retention package

• Provide exclusive discounts

• Assign support executive

""")

        st.balloons()

# ==========================================================
# Analytics Dashboard
# ==========================================================

elif page == "📈 Analytics":

    import plotly.graph_objects as go
    import plotly.express as px

    st.title("📈 Customer Analytics Dashboard")

    st.caption("Business insights based on the current customer profile.")

    st.divider()

    # ===============================
    # KPI Cards
    # ===============================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📅 Tenure",
            f"{st.session_state.tenure} Months"
        )

    with c2:
        st.metric(
            "💰 Monthly Charges",
            f"${st.session_state.monthly_charges:.2f}"
        )

    with c3:
        st.metric(
            "💵 Total Charges",
            f"${st.session_state.total_charges:.2f}"
        )

    with c4:

        avg = st.session_state.total_charges / max(1, st.session_state.tenure)

        st.metric(
            "📈 Avg Monthly Spend",
            f"${avg:.2f}"
        )

    st.divider()

    # ===============================
    # Risk Gauge
    # ===============================

    risk = min(
        100,
        (
            st.session_state.monthly_charges / 120 * 50
            +
            (72 - st.session_state.tenure) / 72 * 50
        )
    )

    gauge = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=risk,

            title={"text": "Estimated Churn Risk"},

            gauge={

                "axis": {"range": [0, 100]},

                "bar": {"color": "#2563eb"},

                "steps": [

                    {"range": [0, 30], "color": "#22c55e"},

                    {"range": [30, 70], "color": "#facc15"},

                    {"range": [70, 100], "color": "#ef4444"}

                ]

            }

        )
    )

    st.plotly_chart(gauge, use_container_width=True)

    st.divider()

    # ===============================
    # Financial Overview
    # ===============================

    data = pd.DataFrame({

        "Category": [

            "Monthly Charges",

            "Average Spend",

            "Total Charges"

        ],

        "Amount": [

            st.session_state.monthly_charges,

            avg,

            st.session_state.total_charges

        ]

    })

    chart = px.bar(

        data,

        x="Category",

        y="Amount",

        text="Amount",

        color="Category"

    )

    chart.update_layout(height=450)

    st.plotly_chart(chart, use_container_width=True)

    st.divider()

    # ===============================
    # Services Pie Chart
    # ===============================

    services = [

        st.session_state.phone_service,

        st.session_state.online_security,

        st.session_state.online_backup,

        st.session_state.device_protection,

        st.session_state.tech_support,

        st.session_state.streaming_tv,

        st.session_state.streaming_movies

    ]

    enabled = services.count("Yes")

    disabled = len(services) - enabled

    pie = px.pie(

        names=["Enabled", "Disabled"],

        values=[enabled, disabled],

        title="Subscribed Services"

    )

    st.plotly_chart(pie, use_container_width=True)

    st.divider()

    # ===============================
    # Customer Overview
    # ===============================

    st.subheader("📋 Customer Overview")

    if risk < 30:

        st.success("""

### 🟢 Low Risk Customer

- Excellent retention probability

- Continue loyalty rewards

- Offer premium services

- High customer satisfaction

""")

    elif risk < 70:

        st.warning("""

### 🟡 Medium Risk Customer

- Moderate churn probability

- Improve customer engagement

- Offer personalized discounts

- Monitor customer activity

""")

    else:

        st.error("""

### 🔴 High Risk Customer

- Immediate retention required

- Contact customer

- Assign support executive

- Offer exclusive discount plan

""")

# ==========================================================
# Reports Page
# ==========================================================

elif page == "📄 Reports":

    import pandas as pd

    st.title("📄 Customer Report")

    st.caption("Generate a business report for the selected customer.")

    st.divider()

    # ========================================
    # Customer Information
    # ========================================

    report = pd.DataFrame({

        "Feature":[
            "Gender",
            "Senior Citizen",
            "Partner",
            "Dependents",
            "Tenure (Months)",
            "Phone Service",
            "Multiple Lines",
            "Internet Service",
            "Online Security",
            "Online Backup",
            "Device Protection",
            "Tech Support",
            "Streaming TV",
            "Streaming Movies",
            "Contract",
            "Paperless Billing",
            "Payment Method",
            "Monthly Charges",
            "Total Charges"
        ],

        "Value":[
            st.session_state.gender,
            st.session_state.senior_citizen,
            st.session_state.partner,
            st.session_state.dependents,
            st.session_state.tenure,
            st.session_state.phone_service,
            st.session_state.multiple_lines,
            st.session_state.internet_service,
            st.session_state.online_security,
            st.session_state.online_backup,
            st.session_state.device_protection,
            st.session_state.tech_support,
            st.session_state.streaming_tv,
            st.session_state.streaming_movies,
            st.session_state.contract,
            st.session_state.paperless_billing,
            st.session_state.payment_method,
            f"${st.session_state.monthly_charges:.2f}",
            f"${st.session_state.total_charges:.2f}"
        ]

    })

    st.subheader("📋 Customer Information")

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ========================================
    # Business Summary
    # ========================================

    avg = st.session_state.total_charges / max(1, st.session_state.tenure)

    st.subheader("📊 Business Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Tenure", f"{st.session_state.tenure} Months")

    with c2:
        st.metric("Monthly Charges", f"${st.session_state.monthly_charges:.2f}")

    with c3:
        st.metric("Average Spend", f"${avg:.2f}")

    st.divider()

    # ========================================
    # AI Recommendation
    # ========================================

    st.subheader("💡 AI Recommendation")

    if st.session_state.contract == "Month-to-month":

        st.warning("""
### Medium Retention Risk

Recommendations:

- Convert customer to yearly contract
- Provide loyalty discount
- Offer premium support
- Increase customer engagement
""")

    else:

        st.success("""
### Stable Customer

Recommendations:

- Maintain relationship
- Offer premium services
- Reward long-term loyalty
- Continue engagement campaigns
""")

    st.divider()

    # ========================================
    # Download Report
    # ========================================

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Customer Report",

        data=csv,

        file_name="customer_report.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.success("✅ Report Generated Successfully")

    st.info("The downloaded report can be shared with business teams for customer retention planning.")

# ==========================================================
# About Page
# ==========================================================

else:

    st.title("👩‍💻 About This Project")

    st.markdown("""
## 📊 Customer Churn Prediction Pro

An AI-powered web application that predicts whether a telecom customer is likely to churn using Machine Learning.

This project is designed to help businesses identify high-risk customers, improve retention strategies, and make data-driven decisions.
""")

    st.divider()

    col1, col2 = st.columns([1,2])

    with col1:

        st.image(
            "https://img.icons8.com/fluency/240/artificial-intelligence.png",
            width=180
        )

    with col2:

        st.subheader("👩‍💻 Developer")

        st.markdown("""
### **Sejal Patole**

🎓 Diploma in Artificial Intelligence & Machine Learning

💡 Aspiring AI/ML Engineer

📍 India

Passionate about building Machine Learning, Deep Learning and Data Science applications that solve real-world business problems.
""")

    st.divider()

    st.subheader("🚀 Project Features")

    c1, c2 = st.columns(2)

    with c1:

        st.success("✔ Customer Churn Prediction")

        st.success("✔ Machine Learning Model")

        st.success("✔ Interactive Dashboard")

        st.success("✔ Business Analytics")

        st.success("✔ Customer Reports")

    with c2:

        st.success("✔ Plotly Charts")

        st.success("✔ Streamlit Web App")

        st.success("✔ CSV Report Download")

        st.success("✔ Modern UI")

        st.success("✔ Business Insights")

    st.divider()

    st.subheader("🛠 Technologies Used")

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.metric("Python", "🐍")

    with tech2:
        st.metric("Streamlit", "🚀")

    with tech3:
        st.metric("Scikit-learn", "🤖")

    with tech4:
        st.metric("Plotly", "📊")

    st.divider()

    st.subheader("📈 Model Information")

    st.info("""
**Algorithm:** Random Forest Classifier

**Dataset:** Telecom Customer Churn Dataset

**Number of Features:** 19

**Target Variable:** Churn (Yes / No)

**Purpose:** Predict customers who are likely to leave the telecom service.
""")

    st.divider()

    st.subheader("🎯 Business Benefits")

    st.markdown("""
- 📉 Reduce customer churn
- 💰 Increase business revenue
- 🤝 Improve customer retention
- 📊 Better business decisions
- 🎯 Target high-risk customers
- 🤖 AI-powered insights
""")

    st.divider()

    st.subheader("📬 Connect With Me")

    st.markdown("""
**GitHub:** https://github.com/sejalpatole

**LinkedIn:** https://www.linkedin.com/in/sejal-patole-317a55323

""")

    st.divider()

    st.success("⭐ Thank you for exploring Customer Churn Prediction Pro!")

    st.caption("© 2026 | Developed by Sejal Patole")
