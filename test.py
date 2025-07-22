import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Crypto Price Viewer")

df = pd.DataFrame({
    "Time": pd.date_range(end=pd.Timestamp.now(), periods=10, freq="H"),
    "Price": [41000 + i * 100 for i in range(10)]
})

fig = px.line(df, x="Time", y="Price", title="Sample Bitcoin Trend")
st.plotly_chart(fig)

