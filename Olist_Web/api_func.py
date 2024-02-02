from fastapi import FastAPI
import numpy as np 
from make_pred import make_prediction
# from train_model import make_model_save
# from make_pred import make_prediction

app = FastAPI()

@app.get("/")
def read_root():
    print("test")
    return("test du backeux")

@app.get("/Prediction/{produit_reçu}")
def get_pred(produit_recu):
    prediction = make_prediction({produit_recu})
    return {prediction}
