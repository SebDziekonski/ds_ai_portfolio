import streamlit as st
from streamlit_option_menu import option_menu
from pycaret.regression import load_model, predict_model
from pycaret.datasets import get_data
import pandas as pd
import plotly.express as px
from dotenv import dotenv_values

# Load environment variables
config = dotenv_values(".env")

# Set OpenAI API key (if using any OpenAI feature later)
if "OPENAI_API_KEY" not in st.session_state:
    if "OPENAI_API_KEY" in config:
        st.session_state["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
    else:
        st.error("OpenAI API key is missing in .env file or session state!")

# Load saved PyCaret model
def load_saved_model():
    return load_model("v3_insurance_prediction_model")

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Insurance Predictor",
        options=["Home", "Check Your Insurance", "Audio Form Completion"],
        icons=["house", "list-task", "mic"],
        menu_icon="cast",
        default_index=0,
    )

# Home Page
if selected == "Home":
    st.title("Welcome to Insurance Charge Predictor")
    st.write("""
       This app predicts your insurance charges based on age, BMI, smoking status, and more.
       Explore the sample data below to see how various factors affect charges.
    """)

    data = get_data('insurance')
    st.dataframe(data.head(15))
    fig = px.histogram(data, x='charges', title="Distribution of Insurance Charges")
    st.plotly_chart(fig)

    st.write("""
        Curious what your predicted insurance charge might be?
        Click the button below to fill out a quick form and find out!
    """)

    if st.button("Go to Check Your Insurance"):
        st.session_state["page"] = "Check Your Insurance"
        st.experimental_rerun()

# Check Your Insurance Page
elif selected == "Check Your Insurance":
    st.title("Check Your Insurance Charge")
    st.write("Complete the form below to estimate your insurance cost.")

    # Inputs
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    sex = st.selectbox("Sex", options=['Male', 'Female'])
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
    children = st.number_input("Number of children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Do you smoke?", options=['Yes', 'No'])
    region = st.selectbox("Region", options=['Southwest', 'Southeast', 'Northwest', 'Northeast'])

    bmi = weight / (height / 100) ** 2
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    st.write("Your information:", input_data)

    if 'model_loaded' not in st.session_state:
        with st.spinner("Loading model..."):
            best_model = load_saved_model()
        st.session_state['model_loaded'] = True
        st.success("Model loaded successfully.")
    else:
        best_model = load_saved_model()

    if st.button("Predict Insurance Charge"):
        prediction = predict_model(best_model, data=input_data)

        # Get prediction
        predicted_cost = prediction.get('Label', [None])[0] if 'Label' in prediction else prediction.get('prediction_label', [None])[0]

        if predicted_cost is not None:
            st.success(f"Your predicted insurance charge is: ${predicted_cost:.2f}")

            st.subheader("Tips to Decrease Insurance Charges:")
            tips = []

            if bmi > 30:
                tips.append("Lower your BMI below 30 through regular exercise and a balanced diet.")
            elif bmi >= 25:
                tips.append("Consider lowering your BMI below 25 to reduce costs.")

            if smoker == "Yes":
                tips.append("Quitting smoking can significantly lower your insurance costs.")

            if age >= 50:
                tips.append("Stay active and attend regular health checkups.")

            if children > 0:
                tips.append("Explore family insurance plans to potentially save money.")

            if not tips:
                st.write("No specific tips – your profile is already optimized!")
            else:
                for tip in tips:
                    st.write(f"- {tip}")
        else:
            st.error("Prediction failed. Please try again.")

# Audio Form Placeholder Page
elif selected == "Audio Form Completion":
    st.title("Audio Form Completion (Coming Soon)")
    st.write("""
        The audio-based form filling feature is currently under development.
        Soon, you'll be able to speak your information instead of typing it manually!
    """)

