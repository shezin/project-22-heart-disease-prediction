import streamlit as st
import pandas as pd
import numpy as np
import random
import pickle

model = pickle.load(open('decision_model.sav','rb'))
def app():
    st.title("HEART DISEASE PREDICTOR")
    age = st.text_input("Age")
    sex = st.selectbox("Sex",('Male','Female'))
    if sex=="Male":
        sex=1
    if sex=="Female":
        sex=0    
    bp = st.text_input("cp")
    trest = st.text_input("trestbps")
    chol = st.text_input("cholesterol")
    fbs = st.text_input("fbs")
    dpf = st.text_input("restecg")
    tha = st.text_input("thalach")
    exa = st.text_input("exang")
    old = st.text_input("oldpeak")
    slope = st.text_input("slope")
    ca = st.text_input("ca")
    thal = st.text_input("thal")

    if st.button("Check Result"):
        rslt = disease_checker(age,sex,bp,trest,chol,fbs,dpf,tha,exa,old,slope,ca,thal)
        st.success(rslt)

#function to check Heart Disease
def disease_checker(age,sex,bp,trest,chol,fbs,dpf,tha,exa,old,slope,ca,thal):
    input = [age,sex,bp,trest,chol,fbs,dpf,tha,exa,old,slope,ca,thal]
    arr = np.array(input)
    prediction = model.predict(arr.reshape(1,-1))
    if prediction == 1:
        return "Test result Positive"
    else:
        return "Test result Negative"