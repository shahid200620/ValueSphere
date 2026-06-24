\# Executive Summary



\## Objective



The objective of this project was to analyze customer behavior and identify meaningful customer segments for targeted marketing strategies while predicting customer lifetime value.



\---



\## Methodology



The project began with synthetic data generation for demographics and transactions.



Data cleaning included:



\* Income imputation using median values by age group

\* Removal of negative transactions

\* Outlier capping using the IQR method



RFM metrics were created:



\* Recency

\* Frequency

\* Monetary



These features were combined into a customer-level analytical base table.



K-Means clustering was applied after standard scaling. The optimal number of clusters was selected using the Elbow Method and Silhouette Score.



Linear Regression was used to predict customer lifetime value.



ANOVA was used to validate whether customer segments showed significant differences in spending behavior.



\---



\## Cluster Profiles



\### Cluster 0 — High-Value Loyalists



Frequent buyers with high spending and recent activity.



\### Cluster 1 — New Potential Buyers



Recently joined customers with moderate spending.



\### Cluster 2 — At-Risk Customers



Customers with high recency and declining activity.



\### Cluster 3 — Frequent Low-Spenders



Active customers but lower average spending.



\---



\## Business Recommendations



\### 1. Reward Loyal Customers



Offer exclusive discounts and premium memberships to retain high-value loyalists.



\### 2. Re-engage At-Risk Customers



Launch email campaigns and special promotions to bring back inactive customers.



\### 3. Upsell Frequent Low-Spenders



Recommend bundle offers and premium products to increase average order value.



\### 4. Nurture New Customers



Provide onboarding offers and personalized product suggestions to improve retention.



