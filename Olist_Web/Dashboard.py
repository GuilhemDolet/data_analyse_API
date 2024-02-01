import streamlit as st
import pandas as pd



# CSV to DataFrame 
olist_df = pd.read_csv('DataSet\TrainingDataSet.csv')
olist_df = pd.DataFrame(olist_df)
olist_df = olist_df.head(20)

########## HTML pour placer un background image #########
def set_bg_hack_url(lien):
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url({lien});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )



def title(text):
     st.markdown(f'<p style="background-color:rgba(169,169,169, 0.8);color:white;font-size:30px;border-radius:10px;text-align:center;">{text}</p>', unsafe_allow_html=True)
def paragraphe(text):
     st.markdown(f'<p style="background-color:rgba(169,169,169, 0.8);color:white;font-size:24px;border-radius:10px;text-align:center;">{text}</p>', unsafe_allow_html=True)


#########################################################


st.set_page_config(page_title="Olist Analyse",page_icon=":shark:")
set_bg_hack_url("https://i.pinimg.com/originals/de/05/93/de0593b47a2eabfccb969b205830b508.jpg")
st.header("BRAZIL OLIST FOREVER")
title("The art of Brazilian's E-commerce:")
paragraphe("Have you received your order?")
st.dataframe(olist_df, use_container_width=True)
st.image("db_olist.png")

