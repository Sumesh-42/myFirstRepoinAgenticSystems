import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fetch_data import fetch_and_process_data


# Page config
st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("📊 Simple Data Dashboard")

# Load data
df = fetch_and_process_data()

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("🔍 Dataset Preview")
st.dataframe(df.head())

# -----------------------------
# Posts per user
# -----------------------------
st.subheader("📈 Posts per User")

posts_per_user = df.groupby("user_id").size()

fig1, ax1 = plt.subplots()
posts_per_user.plot(kind="bar", ax=ax1)

st.pyplot(fig1)

# -----------------------------
# Post length distribution
# -----------------------------
st.subheader("📊 Post Length Distribution")

fig2, ax2 = plt.subplots()
df["post_length"].plot(kind="hist", bins=20, ax=ax2)

st.pyplot(fig2)