import os
import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Absolute path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "datasets",
    "House-Prices-Data",
    "train.csv"
)

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# Dataset overview
st.header("Dataset Overview")
st.write(df.head())
st.write(f"Shape: {df.shape}")

# SalePrice distribution
st.header("SalePrice Distribution")
fig = px.histogram(df, x="SalePrice", nbins=50, marginal="box")
st.plotly_chart(fig, use_container_width=True)

# Numerical Fetures relation with SalesPrice
st.header("Numerical Features vs SalesPrice")

numerical_features = df.select_dtypes(include=['int64','float64']).columns

feature = st.selectbox("Select the numerical feture", numerical_features)

fig = px.scatter(
    df,
    x=feature,
    y="SalePrice",
    trendline="ols",
    opacity=0.5,
    title=f"{feature} vs SalesPrice"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    df,
    x=feature,
    y="SalePrice",
    opacity=1,
    title=f"{feature} vs SalesPrice"
)

st.plotly_chart(fig, use_container_width=True)

st.header("Correlation with SalePrice")

fig = px.imshow(
    df.corr(numeric_only=True),
    x=numerical_features,
    y=numerical_features
)

st.plotly_chart(fig, use_container_width=True)

corr = (
    df.select_dtypes(include=["int64", "float64"])
      .corr()["SalePrice"]
      .sort_values(ascending=False)
)

st.dataframe(corr)
