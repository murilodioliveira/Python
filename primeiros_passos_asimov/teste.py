import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide", page_title="Dashboard Vendas")

df = pd.read_csv("supermarket_sales.csv", sep=",", decimal=".")

st.title("meu aplicativo")
