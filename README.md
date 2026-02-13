# E-Commerce-Sales-Analytics-Customer-Intelligence-System
Project Overview

This project analyzes customer purchasing behavior using RFM (Recency, Frequency, Monetary) analysis, applies K-Means clustering for customer segmentation, and builds a Churn Prediction Model using Machine Learning.

An interactive dashboard is developed using Streamlit to visualize insights and support business decision-making.

🎯 Business Objective

The goal of this project is to:

Identify high-value customers


Segment customers based on behavior

Predict potential churn

Provide actionable business insights

Visualize results through an interactive dashboard

📂 Dataset

Online Retail Transaction Dataset (1-year transaction data)

Features include:

InvoiceNo

StockCode

Quantity

UnitPrice

InvoiceDate

CustomerID

Country

🔎 Key Steps Performed
1️⃣ Data Cleaning & Preprocessing

Removed missing CustomerID values

Handled negative quantities (returns)

Converted date columns

Created TotalAmount feature

2️⃣ RFM Analysis

Calculated:

Recency

Frequency

Monetary

Segmented customers into:

Champions

Loyal Customers

Regular Customers

At Risk

Lost Customers

3️⃣ K-Means Clustering

Applied log transformation

Standardized features

Used Elbow Method & Silhouette Score

Identified optimal number of clusters

Interpreted clusters with business meaning

4️⃣ Churn Prediction Model

Defined churn using data-driven threshold

Built classification model using:

Logistic Regression

Random Forest

Evaluated using:

Confusion Matrix

Classification Report

ROC Curve

AUC Score

5️⃣ Interactive Dashboard (Streamlit)

Dashboard includes:

KPI metrics

Customer segment distribution

Cluster visualization

RFM distributions

Churn analysis

Interactive filters

📈 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Streamlit

🧠 Key Insights

High Recency strongly correlates with churn.

A small percentage of customers contribute majority revenue.

Cluster-based segmentation improves targeting.

Machine learning effectively identifies at-risk customers.

🏆 Business Recommendations

Offer loyalty programs for VIP customers.

Launch re-engagement campaigns for at-risk customers.

Provide personalized offers based on cluster behavior.

Monitor churn probability regularly.

▶ How to Run the Project
pip install -r requirements.txt
python -m streamlit run app.py

👨‍💻 Author

Madhav Kumawat
B.Tech CSE | Data Analytics Enthusias.
