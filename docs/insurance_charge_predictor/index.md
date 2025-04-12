# Insurance Charge Predictor

The application purpose is to estimate how much money you might have to pay for insurance based on your personal data like age, BMI, smoker status etc.

Also when charge is estimated, application will give the user a hint on what he or she might do to decrease estimated insurance charge. 

# 🧭 Main Features:
## Home Page

- Explains how insurance charges vary.

- Shows a sample dataset (from pycaret.datasets) and a histogram of charges.

## Check Your Insurance

- A form where users manually enter their data:

        -Age, sex, weight, height, children, smoker, and region

- The app calculates BMI (body mass index) from weight/height.

- It then predicts the insurance charge using a trained machine learning model.

- It also gives personalized health tips to potentially lower your insurance premium.

## Audio Form Completion (Currently disabled for now — marked as “coming soon”)

- Intended to let users speak their data and use speech-to-text (STT) to auto-fill the form.

- Uses OpenAI Whisper API to transcribe audio (via openai.audio.transcriptions.create()).

- Also planned: parsing natural language into structured form data.

# 🛠️ Key Tools & Techniques Used
## 🖼️ UI Framework:
- Streamlit: Quickly creates web apps with Python.

## 📦 Model Training & Prediction:
## PyCaret (Regression Module):

- Automates training and saving of regression models.

- The app loads a pre-trained PyCaret model (v3_insurance_prediction_model) to make predictions.

# 📊 Data Visualization:
- Plotly Express: Interactive histogram for visualizing insurance charge distributions.

# 🧮 Machine Learning Techniques:
## The model (trained via PyCaret) likely uses one or more regression techniques like:

- Linear Regression

- Random Forest Regressor

- Gradient Boosting

- PyCaret tries many and chooses the best via cross-validation.

# 📦 Audio & NLP (planned features):
- OpenAI Whisper API: Used for speech-to-text transcription.

- Natural Language Parsing: Planned to convert spoken text into form data using regex-based extraction.

Follow the link below, to see for yourself how the application works:
<br><a href="https://github.com/SebDziekonski/ds_ai_portfolio.git" target="_blank">Open in new tab</a>