import json
import pickle

def make_prediction(x):
    # Charger le modèle à partir d'un fichier Pickle
    with open('main_model.pkl', 'rb') as fichier_modele:   #rb = lecture en mode binaire
            loaded_model = pickle.load(fichier_modele)
    # faire la prédiction
    predicition_out = loaded_model.predict(x)

    # prediction_string = data[str(int(predicition_out))]
    
    return predicition_out