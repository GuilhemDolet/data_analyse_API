import streamlit as st
import pandas as pd
import plotly.express as px
from Dashboard import set_bg_hack_url

cat_product_df = pd.read_csv("DataSet\product_count.csv")

histogram = px.histogram(cat_product_df, x="product_category_name", y="count")

st.plotly_chart(histogram)