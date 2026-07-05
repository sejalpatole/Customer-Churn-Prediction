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

    st.title("👤 Customer Information")

    st.write("Enter customer details for churn prediction.")

    st.divider()

    col1, col2 = st.columns(2)

    # --------------------------
    # Personal Information
    # --------------------------

    with col1:

        st.subheader("Personal Details")

        st.session_state.gender = st.selectbox(
            "Gender",
            ["Female", "Male"],
            index=0 if st.session_state.gender=="Female" else 1
        )

        st.session_state.senior_citizen = st.selectbox(
            "Senior Citizen",
            ["No","Yes"],
            index=0 if st.session_state.senior_citizen=="No" else 1
        )

        st.session_state.partner = st.selectbox(
            "Partner",
            ["No","Yes"],
            index=0 if st.session_state.partner=="No" else 1
        )

        st.session_state.dependents = st.selectbox(
            "Dependents",
            ["No","Yes"],
            index=0 if st.session_state.dependents=="No" else 1
        )

        st.session_state.tenure = st.slider(
            "Tenure (Months)",
            0,
            72,
            st.session_state.tenure
        )

    # --------------------------
    # Services
    # --------------------------

    with col2:

        st.subheader("Customer Services")

        st.session_state.phone_service = st.selectbox(
            "Phone Service",
            ["Yes","No"],
            index=0 if st.session_state.phone_service=="Yes" else 1
        )

        st.session_state.multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No","Yes","No phone service"],
            index=["No","Yes","No phone service"].index(
                st.session_state.multiple_lines
            )
        )

        st.session_state.internet_service = st.selectbox(
            "Internet Service",
            ["DSL","Fiber optic","No"],
            index=["DSL","Fiber optic","No"].index(
                st.session_state.internet_service
            )
        )

        st.session_state.online_security = st.selectbox(
            "Online Security",
            ["No","Yes","No internet service"],
            index=["No","Yes","No internet service"].index(
                st.session_state.online_security
            )
        )

        st.session_state.online_backup = st.selectbox(
            "Online Backup",
            ["No","Yes","No internet service"],
            index=["No","Yes","No internet service"].index(
                st.session_state.online_backup
            )
        )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("Additional Services")

        st.session_state.device_protection = st.selectbox(
            "Device Protection",
            ["No","Yes","No internet service"],
            index=["No","Yes","No internet service"].index(
                st.session_state.device_protection
            )
        )

        st.session_state.tech_support = st.selectbox(
            "Tech Support",
            ["No","Yes","No internet service"],
            index=["No","Yes","No internet service"].index(
                st.session_state.tech_support
            )
        )

        st.session_state.streaming_tv = st.selectbox(
            "Streaming TV",
            ["No","Yes","No internet service"],
            index=["No","Yes","No internet service"].index(
                st.session_state.streaming_tv
            )
        )

        st.session_state.streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No","Yes","No internet service"],
            index=["No","Yes","No internet service"].index(
                st.session_state.streaming_movies
            )
        )

    with col4:

        st.subheader("Billing Information")

        st.session_state.contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ],
            index=[
                "Month-to-month",
                "One year",
                "Two year"
            ].index(st.session_state.contract)
        )

        st.session_state.paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes","No"],
            index=0 if st.session_state.paperless_billing=="Yes" else 1
        )

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
            "Monthly Charges",
            min_value=0.0,
            value=float(st.session_state.monthly_charges)
        )

        st.session_state.total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            value=float(st.session_state.total_charges)
        )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c2:

        if st.button(
            "💾 Save Customer Information",
            use_container_width=True
        ):
            st.success("Customer information saved successfully!")

    

# ==========================================================
# Prediction Page
# ==========================================================

elif page=="🤖 Prediction":

    st.title("🤖 AI Churn Prediction")

    st.write("Run the trained Machine Learning model to predict whether the customer is likely to churn.")

    st.divider()

    if st.button("🚀 Predict Customer Churn", use_container_width=True):

        # -----------------------------
        # Collect Inputs
        # -----------------------------

        input_data = {
            "gender": st.session_state.gender,
            "SeniorCitizen": 1 if st.session_state.senior_citizen=="Yes" else 0,
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
        }

        import pandas as pd

        df = pd.DataFrame([input_data])

        # -----------------------------
        # Encoding
        # -----------------------------

        cat_cols = df.select_dtypes(include="object").columns

        for col in cat_cols:

            if col in encoder:

                df[col] = encoder[col].transform(df[col])

        # -----------------------------
        # Scaling
        # -----------------------------

        df = scaler.transform(df)

        # -----------------------------
        # Prediction
        # -----------------------------

        prediction = model.predict(df)[0]

        probability = model.predict_proba(df)[0][1]

        st.divider()

        st.subheader("Prediction Result")

        if prediction == 1:

            st.error("🚨 Customer is likely to CHURN")

        else:

            st.success("✅ Customer is likely to STAY")

        st.write("")

        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

        st.progress(float(probability))

        st.write("")

        # -----------------------------
        # Risk Level
        # -----------------------------

        if probability < 0.30:

            st.success("🟢 Low Risk Customer")

        elif probability < 0.70:

            st.warning("🟡 Medium Risk Customer")

        else:

            st.error("🔴 High Risk Customer")

        st.divider()

        st.subheader("💡 AI Recommendations")

        if probability < 0.30:

            st.success("""
- Customer appears satisfied.
- Continue current service quality.
- Offer loyalty rewards.
            """)

        elif probability < 0.70:

            st.warning("""
- Offer discount plans.
- Improve customer engagement.
- Recommend value-added services.
            """)

        else:

            st.error("""
- Immediate retention campaign required.
- Contact customer support team.
- Offer premium discounts.
- Assign dedicated relationship manager.
            """)

        st.balloons()


# ==========================================================
# Reports Page
# ==========================================================

elif page=="📈 Analytics":

    import plotly.graph_objects as go
    import plotly.express as px
    import pandas as pd

    st.title("📈 Analytics Dashboard")

    st.write("Business insights generated from customer information.")

    st.divider()

    # ==========================
    # KPI Cards
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Customer Tenure", f"{st.session_state.tenure} Months")

    with c2:
        st.metric("Monthly Charges", f"${st.session_state.monthly_charges:.2f}")

    with c3:
        st.metric("Total Charges", f"${st.session_state.total_charges:.2f}")

    with c4:
        avg = (
            st.session_state.total_charges /
            max(st.session_state.tenure,1)
        )
        st.metric("Avg Monthly Spend", f"${avg:.2f}")

    st.divider()

    # ==========================
    # Gauge Chart
    # ==========================

    risk_score = min(
        100,
        (
            st.session_state.monthly_charges/120*50
            +
            (72-st.session_state.tenure)/72*50
        )
    )

    gauge = go.Figure(go.Indicator(

        mode="gauge+number",

        value=risk_score,

        title={'text':"Estimated Risk Score"},

        gauge={

            'axis':{'range':[0,100]},

            'bar':{'color':'red'},

            'steps':[

                {'range':[0,30],'color':'lightgreen'},

                {'range':[30,70],'color':'gold'},

                {'range':[70,100],'color':'salmon'}

            ]

        }

    ))

    st.plotly_chart(gauge, use_container_width=True)

    st.divider()

    # ==========================
    # Customer Profile
    # ==========================

    profile = pd.DataFrame({

        "Feature":[
            "Tenure",
            "Monthly Charges",
            "Total Charges"
        ],

        "Value":[
            st.session_state.tenure,
            st.session_state.monthly_charges,
            st.session_state.total_charges
        ]

    })

    fig = px.bar(

        profile,

        x="Feature",

        y="Value",

        text="Value",

        color="Feature"

    )

    fig.update_layout(

        title="Customer Financial Profile",

        height=450

    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ==========================
    # Service Distribution
    # ==========================

    services = [

        st.session_state.phone_service,
        st.session_state.online_security,
        st.session_state.online_backup,
        st.session_state.device_protection,
        st.session_state.tech_support,
        st.session_state.streaming_tv,
        st.session_state.streaming_movies

    ]

    yes = services.count("Yes")
    no = len(services)-yes

    pie = px.pie(

        names=["Enabled","Disabled"],

        values=[yes,no],

        title="Subscribed Services"

    )

    st.plotly_chart(pie, use_container_width=True)

    st.divider()

    # ==========================
    # Executive Summary
    # ==========================

    st.subheader("📋 Executive Summary")

    if risk_score < 30:

        st.success("""

### 🟢 Healthy Customer

- Strong retention probability
- Low churn risk
- Continue loyalty programs
- Upsell premium services

""")

    elif risk_score < 70:

        st.warning("""

### 🟡 Medium Risk Customer

- Customer engagement recommended
- Offer personalized discounts
- Improve support quality

""")

    else:

        st.error("""

### 🔴 High Risk Customer

- Immediate retention campaign
- Dedicated support executive
- Premium offers recommended
- High chance of churn

""")
# ==========================================================
# Reports Page
# ==========================================================

elif page=="📄 Reports":

    import pandas as pd

    st.title("📄 Customer Report")

    st.write("Generate a detailed report of the current customer.")

    st.divider()

    report = pd.DataFrame({

        "Feature":[
            "Gender",
            "Senior Citizen",
            "Partner",
            "Dependents",
            "Tenure",
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
            st.session_state.monthly_charges,
            st.session_state.total_charges
        ]

    })

    st.subheader("📋 Customer Information")

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    avg = st.session_state.total_charges / max(st.session_state.tenure,1)

    st.subheader("📊 Business Summary")

    st.info(f"""
Customer Tenure: {st.session_state.tenure} Months

Monthly Charges: ${st.session_state.monthly_charges:.2f}

Total Charges: ${st.session_state.total_charges:.2f}

Average Monthly Spend: ${avg:.2f}

Contract: {st.session_state.contract}

Internet Service: {st.session_state.internet_service}
""")

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Customer Report",
        csv,
        "customer_report.csv",
        "text/csv",
        use_container_width=True
    )
    

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