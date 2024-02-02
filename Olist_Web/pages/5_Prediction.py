import streamlit as st
import numpy as np
# from make_pred import make_prediction
import json
import pandas as pd
import plotly.express as px
import requests

st.sidebar.header("Make prediction")

produit_reçu = st.sidebar.text_input("Avez-vous reçu votre produit ?")
make_pred_API = st.sidebar.button("Predict")

if make_pred_API: 
    #construire l'URL avec les paramètres => appel (get)
    url = f"http://localhost:8501/Prediction/{str(produit_reçu)}"
    # Envoyer la requête à FastAPI
    response = requests.get(url)
    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Prediction result: {prediction}")
    else: 
        st.error("Error in prediction request")

        