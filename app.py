import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="ValueSphere Dashboard", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv("data/processed/abt.csv")


abt = load_data()

st.title("Customer Segmentation and Lifetime Value Dashboard")

st.sidebar.header("Filters")

selected_cluster = st.sidebar.multiselect(
    "Select Cluster",
    options=abt["Cluster"].unique(),
    default=abt["Cluster"].unique()
)

filtered_data = abt[abt["Cluster"].isin(selected_cluster)]

st.header("Overview")

st.write("Total Customers:", filtered_data.shape[0])
st.write("Average Monetary Value:", round(filtered_data["Monetary"].mean(), 2))
st.write("Average Frequency:", round(filtered_data["Frequency"].mean(), 2))


st.header("Customer Segments")

st.subheader("1. Income vs Monetary by Cluster")

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=filtered_data,
    x="income",
    y="Monetary",
    hue="Cluster",
    ax=ax1
)
st.pyplot(fig1)


st.subheader("2. Recency Distribution by Cluster")

fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.boxplot(
    data=filtered_data,
    x="Cluster",
    y="Recency",
    ax=ax2
)
st.pyplot(fig2)


st.subheader("3. Customer Distribution")

cluster_counts = filtered_data["Cluster"].value_counts()

fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.pie(
    cluster_counts,
    labels=cluster_counts.index,
    autopct="%1.1f%%"
)
st.pyplot(fig3)


st.header("Value Prediction")

st.subheader("4. Monetary by Cluster")

fig4, ax4 = plt.subplots(figsize=(8, 5))
filtered_data.groupby("Cluster")["Monetary"].mean().plot(
    kind="bar",
    ax=ax4
)
st.pyplot(fig4)


st.subheader("5. Frequency vs Recency")

fig5, ax5 = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=filtered_data,
    x="Frequency",
    y="Recency",
    hue="Cluster",
    ax=ax5
)
st.pyplot(fig5)