import streamlit as st
import pandas as pd
import plotly.express as px
from Dashboard import set_bg_hack_url, title, paragraphe
import matplotlib.pyplot as plt
import seaborn as sns

olist_df = pd.read_csv('DataSet\TrainingDataSet.csv')

set_bg_hack_url("https://wallpaperaccess.com/full/4695093.jpg")
st.header('Observation de la distribution des notes attribuées aux commandes', divider='gray')
count_plot = px.histogram(
    (olist_df),
    x = "review_score",
    color = "review_score",
    # title = "totale des notes obtenues",
    color_discrete_map={1: '#012169', 2: '#009739', 3: '#FFFFFF', 4:'orange', 5:'#FEDD00'}
    # color_discrete_sequence=['indianred']
)
st.plotly_chart(count_plot)

paragraphe("Création de la variable 'score' (0: non, 1:oui) les notes de 5 sont considérées satisfaisantes. Toutes les autres non-satisfaisantes.")

##### Création d'un graphique seaborn ######

plt.figure(figsize=(5, 4))
ax = sns.countplot(x='score', data=olist_df, palette='viridis')

# Add percentages to each bar
total = len(olist_df['score'])
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height() / total)
    # percentage = 100 * p.get_height() / total
    print(type(percentage))
    x = p.get_x() + p.get_width() / 2 
    y = p.get_height() + 1000
    ax.annotate(percentage, (x, y), ha='center')


ax.set_title('Distribution des notes attribuées aux commandes')
ax.set_xlabel('satisfaction')
ax.set_ylabel('Fréquence')

# On stock le résultat sous forme d'image
st.image("pages\output.png")
