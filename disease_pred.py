from streamlit_option_menu import option_menu
import streamlit as st
import numpy as np
import pandas as pd
import pickle

pickle_in = open("heart_disease_prediction (1).pkl", "rb")
model=pickle.load(pickle_in)


# Create a sidebar menu
with st.sidebar:
    selected = option_menu(menu_title="MainMenu",options=["Home",  "Predictor", "Healthy Diet Tips"],
                           icons=['house',  'activity', 'heart'],
                           menu_icon="cast", default_index=0)

# Home page with wallpaper and quote
if selected == "Home":
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/001/592/183/datas/original.jpg"); /* Replace with your wallpaper URL */
            background-size: cover;
            background-position: 90% 90%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Predictor page
elif selected == "Predictor":
    st.title("Heart Disease Prediction")

    # Create input fields


    age = st.number_input("Age (1 to 100)", min_value=0, max_value=100, step=1, help="Enter the patient's age.")
    sex = st.selectbox("Sex", options=["Female", "Male"], help="Select the patient's gender.")
    cp = st.number_input("Chest Pain Type (1-4)", min_value=1, max_value=4, step=1, help="Chest pain type (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic).")
    trestbps = st.number_input("Resting Blood Pressure (mm Hg) (94-200)", min_value=94, max_value=200, help="Resting blood pressure in mm Hg on admission to the hospital.")
    chol = st.number_input("Serum Cholesterol (mg/dl) (126-564)", min_value=126, max_value=564, help="Serum cholesterol in mg/dl.")
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=["No", "Yes"], help="Is fasting blood sugar > 120 mg/dl? (No = 0, Yes = 1).")
    restecg = st.number_input("Resting Electrocardiographic Results (0-2)", min_value=0, max_value=2, step=1, help="Resting electrocardiographic results (0: normal, 1: having ST-T wave abnormality, 2: showing probable or definite left ventricular hypertrophy by Estes' criteria).")
    thalach = st.number_input("Maximum Heart Rate Achieved (71-202)", min_value=71, max_value=202, help="Maximum heart rate achieved during exercise.")
    exang = st.selectbox("Exercise Induced Angina", options=["No", "Yes"], help="Exercise induced angina (No = 0, Yes = 1).")
    oldpeak = st.number_input("ST Depression Induced by Exercise (0-6.2)", min_value=0.0, max_value=6.2, step=0.1, help="ST depression induced by exercise relative to rest.")
    slope = st.number_input("Slope of the Peak Exercise ST Segment (1-3)", min_value=1, max_value=3, step=1, help="The slope of the peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping).")
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", min_value=0, max_value=3, step=1, help="Number of major vessels (0-3) colored by fluoroscopy.")
    thal = st.number_input("Thallium Stress Test Result (3-7)", min_value=3, max_value=7, step=1, help="Thallium stress test result (3: normal, 6: fixed defect, 7: reversible defect).")

    # Map input values to model input
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    exang = 1 if exang == "Yes" else 0

    # Prediction
    if st.button("Predict"):
        arr = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        pred = model.predict(arr)
        
        if pred == 0:
            res_val = "Your cardiovascular health is in GOOD CONDITION. Maintaining healthy habits is key to keeping it that way🥳.ST"
        else:
            res_val = "You have been DIAGNOSED WITH HEART DISEASE. It's essential to prioritize your health and well-being."
        
        st.write(f"{res_val}")

# Healthy Diet Tips page
elif selected == "Healthy Diet Tips":
    tips = [
        {
            "image": "https://th.bing.com/th/id/R.171469519d57e63bf0cb18c3257797e3?rik=Rs1FirAHPKiyXA&riu=http%3a%2f%2fwww.baltana.com%2ffiles%2fwallpapers-2%2fFruit-HD-Wallpapers-03484.jpg&ehk=7L0lkg9TPcRVu%2bjsZhWvhNw1CZRgILylaYrEFKMa6n4%3d&risl=&pid=ImgRaw&r=0",
            "description": "Eat a healthy diet rich in fruits, vegetables, and whole grains."
        },
        {
            "image": "https://th.bing.com/th/id/OIP.8QEbwOsxecLInhWvXOtodwAAAA?rs=1&pid=ImgDetMain",
            "description": "Exercise regularly. Aim for at least 30 minutes of moderate exercise most days of the week."
        },
        {
            "image": "https://thumbs.dreamstime.com/z/no-smoking-alcohol-drinking-vector-sign-caution-120183609.jpg",
            "description": "Avoid smoking and limit alcohol intake."
        },
        {
            "image": "https://images.hindustantimes.com/img/2023/01/20/1600x900/healthy_weight_1674201407133_1674201417707_1674201417707.jpg",
            "description": "Maintain a healthy weight to reduce stress on your heart."
        },
        {
            "image": "https://th.bing.com/th/id/OIP.-YA91mo2AK-L8hWgeQJbKgHaE8?rs=1&pid=ImgDetMain",
            "description": "Monitor your blood pressure and cholesterol levels."
        },
        {
            "image": "https://th.bing.com/th/id/OIP.Yioh7nrjP5NPzYwy-1NEqwHaEK?rs=1&pid=ImgDetMain",
            "description": "Get enough sleep. Adults should aim for 7-9 hours per night."
        }
    ]

    # Set the title
    st.title("Healthy Tips")

    # Loop through each tip and display it with consistent image size and readable description
    for tip in tips:
        st.write("")
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(tip["image"], use_column_width=True)
        with col2:
            st.write(tip["description"])
        st.write("")
