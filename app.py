import streamlit as st
import plotly.graph_objects as go
import mysql.connector
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os
from db_config import connect_db

conn = connect_db()
cursor = conn.cursor()

# UI
st.title("📊 Crypto Price Tracker")
conn = connect_db()
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT COIN FROM CRYPTO ORDER BY COIN")
coins = [row[0] for row in cursor.fetchall()]
selected_coin = st.selectbox("Select a coin", coins)

# Fetch data
cursor.execute("SELECT PRICE, TIMESTAMP FROM CRYPTO WHERE COIN = %s ORDER BY ID DESC LIMIT 50", (selected_coin,))
data = cursor.fetchall()
cursor.close()
conn.close()

if not data:
    st.warning("No data available.")
    st.stop()

# Prepare data
df = pd.DataFrame(data, columns=["Price", "Timestamp"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values("Timestamp")

prices = df["Price"].tolist()
timestamps = df["Timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S").tolist()

def format_price(p):
    if p < 1:
        return f"₹{p:.4f}"
    elif p < 500:
        return f"₹{p:.2f}"
    else:
        return f"₹{p:,.0f}"

# Stats
avg_price = sum(prices) / len(prices)
min_price = min(prices)
max_price = max(prices)

stats_text = (
    f"Points: {len(prices)}\n"
    f"Avg: {format_price(avg_price)}\n"
    f"Max: {format_price(max_price)}\n"
    f"Min: {format_price(min_price)}"
)

# Plotly chart
fig = go.Figure()

# Custom hover text based on price value
hover_texts = []
for p in prices:
    if p < 1:
        hover_texts.append(f"₹{p:.4f}")
    elif p < 500:
        hover_texts.append(f"₹{p:.2f}")
    else:
        hover_texts.append(f"₹{p:,.0f}")


fig.add_trace(go.Scatter(
    x=timestamps,
    y=prices,
    mode='lines+markers',
    name=selected_coin.capitalize(),
    marker=dict(size=6, color='dodgerblue'),
    line=dict(color='royalblue', width=2),
    hovertext=hover_texts,
    hovertemplate='%{hovertext}<extra></extra>'
))

fig.update_layout(
    title=f"{selected_coin.title()} Price Over Time",
    xaxis_title="Time",
    yaxis_title="Price (INR)",
    template="plotly_dark",
    hovermode="x unified",
    margin=dict(l=40, r=20, t=50, b=40),
    annotations=[
        dict(
            x=0.99, y=1.05,
            xref="paper", yref="paper",
            text=stats_text,
            showarrow=False,
            font=dict(size=14, color="white"),
            align="right",
            bgcolor="gray",
            opacity=0.7
        )
    ]
)

st.plotly_chart(fig, use_container_width=True)
