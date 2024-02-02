import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pickle

def make_model_save():
    olist_df = pd.read_csv('Olist_Web\DataSet\TrainingDataSet.csv')
    print(olist_df.head())

    y = olist_df['score']
    x = olist_df[["produit_recu"]]
    X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

    model = RandomForestClassifier(max_depth=2, random_state=0)

    model.fit(X_train,y_train)

    with open('main_model.pkl', 'wb') as fichier_modele:
        pickle.dump(model, fichier_modele)

    predictions = model.predict(X_test)
    print(f"MAE: {str(mean_absolute_error(predictions, y_test))}")


