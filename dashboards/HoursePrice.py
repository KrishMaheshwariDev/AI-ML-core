import os
import streamlit as st
import pandas as pd
import plotly.express as px
# import statsmodels.api as sm
# import matplotlib.pyplot as plt
# import seaborn as sns

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

# SideBar Panel
st.sidebar.header("EDA controls")
target = st.sidebar.selectbox("Select the Target Column", options=df.columns)

# Variables

num_features = []
cat_features = []

if target in df.select_dtypes(include=["object"]).columns:
    num_features = df.select_dtypes(include=["int64", "float64"]).columns.drop('Id')
    cat_features = df.select_dtypes(include="object").columns.drop(target)
else:
    num_features = df.select_dtypes(include=["int64", "float64"]).columns.drop([target, "Id"])
    cat_features = df.select_dtypes(include="object").columns

# Tabs Section

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Distributions",
    "Relationships",
    "Correlation & Risk"
])

# Tab1 : Overview
with tab1:
    st.header("Dataset Overview")
    st.write(df.head(10))
    st.write(f"Shape: {df.shape}")

# Tab2 : Distributions
with tab2:
    feature = st.selectbox("Select the Numerical Feature", num_features)

    col1, col2 = st.columns([3,1])

    with col1:
        fig = px.histogram(
            df,
            x=feature,
            nbins=50,
            title=f"Distribution of {feature}"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.box(
            df,
            y=feature,
            title=f"Outliers of {feature}"
        )

        st.plotly_chart(fig, use_container_width=True)

# Tab 3: Relationships

with tab3:
    feature = st.selectbox("Select the Feature", num_features)

    fig = px.scatter(
        df,
        x=feature,
        y=target,
        trendline="ols",
        opacity=0.5,
        title=f"{feature} vs {target}"
    )

    st.plotly_chart(fig, use_container_width=True)

# Tab 4: correlations

with tab4:
    st.header("Top Correlated Features")

    k = st.slider("Top K features", 5, 10, 20)

    corr = (
        df.select_dtypes(include=["int64", "float64"])
        .corr()[target]
        .drop(target)
        .sort_values(ascending=False)
        .head(k)
    )

    fig = px.bar(
        corr,
        x=corr.values,
        y=corr.index,
        orientation="h",
        title=f"Top {k} Correlated features with {target}"
    )

    st.plotly_chart(fig, use_container_width=True)
