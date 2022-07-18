import streamlit as st

def app():
    st.title('-HEART DISEASE PREDICTION')
    st.header("Attributes")
    st.text("**age - age in years\n"
    "**cp - (chest pain type)  0: Typical angina: chest pain related decrease blood supply to the heart 1: Atypical angina: chest pain not related to heart\n                            "
    "2: Non-anginal pain: (non heart related)"
    "3: Asymptomatic: chest pain not showing signs of disease\n"
    "**trestbps- resting blood pressure (in mm Hg)\n"
    "**chol - serum cholestoral in mg/dl\n"
    "**fbs - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)\n"
    "**restecg - resting electrocardiographic results 0: Normal 1: ST Wave abnormality 2:ventricular hypertrophy\n"
    "**thalach - maximum heart rate achieved\n"
    "**exang - exercise induced angina (1 = yes; 0 = no)\n"
    "**oldpeak - ST depression induced by exercise 0: Upsloping(better),1: Flatsloping,2: Downsloping(unhealthy heart)\n"
    "**ca - number of major vessels (0-3) colored by flourosopy\n"
    "**thal - thalium stress result 0,1: normal 2: fixed defect: (used to be defect but ok now) 3: reversable defect(No proper blood movement)\n "
    
    )
    