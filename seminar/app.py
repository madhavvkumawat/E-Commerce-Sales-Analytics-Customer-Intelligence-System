import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Customer Analytics Dashboard",
                   layout="wide")

st.title("📊 Customer Analytics Dashboard")
st.markdown("RFM Analysis | Clustering | Churn Prediction")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("final_customer_data.csv")

df = load_data()

# Sidebar filter
st.sidebar.header("Filters")

selected_segment = st.sidebar.multiselect(
    "Select Segment",
    options=df['Segment'].unique(),
    default=df['Segment'].unique()
)

filtered_df = df[df['Segment'].isin(selected_segment)]

# =========================
# KPI Section
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", filtered_df['CustomerID'].nunique())
col2.metric("Total Revenue", f"${filtered_df['Monetary'].sum():,.0f}")
col3.metric("Avg Revenue per Customer",
            f"${filtered_df['Monetary'].mean():,.0f}")
col4.metric("Churn Rate",
            f"{filtered_df['Churn'].mean()*100:.2f}%")

st.markdown("---")

# =========================
# Segment Distribution
# =========================

st.subheader("Customer Segment Distribution")

fig1, ax1 = plt.subplots()
filtered_df['Segment'].value_counts().plot(kind='bar', ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# =========================
# Cluster Distribution
# =========================

st.subheader("Cluster Distribution")

fig2, ax2 = plt.subplots()
filtered_df['Cluster'].value_counts().plot(kind='bar', ax=ax2)
st.pyplot(fig2)

# =========================
# RFM Distributions
# =========================

st.subheader("RFM Distributions")

col5, col6, col7 = st.columns(3)

with col5:
    fig_r, ax_r = plt.subplots()
    ax_r.hist(filtered_df['Recency'], bins=30)
    ax_r.set_title("Recency")
    st.pyplot(fig_r)

with col6:
    fig_f, ax_f = plt.subplots()
    ax_f.hist(filtered_df['Frequency'], bins=30)
    ax_f.set_title("Frequency")
    st.pyplot(fig_f)

with col7:
    fig_m, ax_m = plt.subplots()
    ax_m.hist(filtered_df['Monetary'], bins=30)
    ax_m.set_title("Monetary")
    st.pyplot(fig_m)

# =========================
# Churn Analysis
# =========================

st.subheader("Churn Analysis")

fig3, ax3 = plt.subplots()
filtered_df['Churn'].value_counts().plot(kind='pie',
                                         autopct='%1.1f%%',
                                         ax=ax3)
ax3.set_ylabel("")
st.pyplot(fig3)

st.markdown("### Churn Rate by Segment")

churn_segment = filtered_df.groupby('Segment')['Churn'].mean()

fig4, ax4 = plt.subplots()
churn_segment.plot(kind='bar', ax=ax4)
st.pyplot(fig4)

st.markdown("---")
st.markdown("Developed by Madhav Kumawat 🚀")
