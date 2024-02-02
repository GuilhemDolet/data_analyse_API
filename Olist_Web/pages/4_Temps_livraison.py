import streamlit as st
import pandas as pd
import plotly.express as px

livraison_df = pd.read_csv("DataSet/temps_livraison.csv")

histo_livraison = px.histogram((livraison_df), x="temps_livraison", range_x=[0, 50])
st.plotly_chart(histo_livraison)

