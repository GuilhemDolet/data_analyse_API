import streamlit as st
import pandas as pd
import plotly.express as px
from Dashboard import set_bg_hack_url
import folium
from streamlit_folium import folium_static


set_bg_hack_url("https://hdwallpaperim.com/wp-content/uploads/2017/08/25/455641-space-stars-galaxy-nebula-space_art.jpg")
geoloc_df = pd.read_csv('DataSet\geolocalisation_customer.csv')

# Création de la carte Folium
latitude_center = geoloc_df['geolocation_lat'].iloc[0]
longitude_center = geoloc_df['geolocation_lng'].iloc[0]
ma_carte = folium.Map(location=[latitude_center, longitude_center], zoom_start=6)

# Ajout de marqueurs pour chaque point de latitude et longitude dans le DataFrame
for index, row in geoloc_df.iterrows():
    # Ajout du nombre de clients ou de commandes au popup
    popup_text = f"Nombre de Client: {row['customer_unique_id']}"
    # Ajout du marqueur avec le popup
    folium.Marker([row['geolocation_lat'], row['geolocation_lng']], popup=popup_text).add_to(ma_carte)

folium_static(ma_carte)

