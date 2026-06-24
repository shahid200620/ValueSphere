\# ValueSphere



\## Customer Segmentation and Lifetime Value Prediction



ValueSphere is a data science project focused on analyzing customer behavior using demographic and transaction data. The project applies data cleaning, RFM analysis, customer segmentation using K-Means clustering, lifetime value prediction using Linear Regression, and statistical validation using ANOVA.



The goal is to help businesses move from generic marketing strategies to targeted customer-focused campaigns.



\---



\## Business Problem



Companies collect customer data but often fail to transform it into actionable insights. This project helps identify valuable customer groups and predicts their future value to improve marketing efficiency and customer retention.



\---



\## Project Structure



ValueSphere/



├── data/



│   ├── raw/



│   └── processed/



├── notebooks/



│   └── customer\_analysis.ipynb



├── src/



│   ├── generate\_data.py



│   └── data\_preprocessing.py



├── app.py



├── requirements.txt



├── report.md



└── README.md



\---



\## Setup Instructions



\### Clone Repository



git clone https://github.com/shahid200620/ValueSphere.git



cd ValueSphere



\---



\### Create Virtual Environment



python -m venv venv



venv\\Scripts\\activate



\---



\### Install Dependencies



pip install -r requirements.txt



\---



\### Generate Synthetic Data



python src\\generate\_data.py



This creates:



\* demographics.csv

\* transactions.csv



inside data/raw/



\---



\### Run Notebook



jupyter notebook



Open:



notebooks/customer\_analysis.ipynb



Run all cells.



\---



\### Run Streamlit Dashboard



streamlit run app.py



\---



\## Methods Used



\* Data Cleaning

\* Missing Value Imputation

\* Outlier Treatment (IQR)

\* RFM Analysis

\* Standard Scaling

\* K-Means Clustering

\* Elbow Method

\* Silhouette Score

\* Linear Regression

\* ANOVA Testing



\---



\## Outputs



\* Customer Segments

\* LTV Predictions

\* Interactive Dashboard

\* Business Recommendations



