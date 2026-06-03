Online Retail Customer Analytics Dashboard

Project Summary

This project analyzes customer purchasing behavior, revenue trends, customer lifetime value (CLV), customer retention, and product performance using the Online Retail dataset.

The objective of this project is to transform raw retail sales data into meaningful business insights through data analysis, customer segmentation, retention analysis, and interactive dashboards.

Project Tools

- Python
- Pandas
- PostgreSQL
- Power BI
- Matplotlib
- seaborn


Implementation Steps

Raw Data
→ Data Inspection
→ Data Cleaning
→ Feature Engineering
→ Exploratory Data Analysis (EDA)
→ SQL Analytics
→ RFM Customer Segmentation
→ Customer Retention (Cohort Analysis)
→ Customer Lifetime Value (CLV) Analysis
→ Power BI Dashboard Development

Analysis Sections

Data Inspection
- Examined dataset structure and data quality.
- Identified missing values, duplicates, and invalid records.

Data Cleaning
- Removed cancelled transactions.
- Handled missing values.
- Removed duplicate records.
- Standardized data formats.

Exploratory Data Analysis (EDA)
- Analyzed revenue trends.
- Evaluated customer purchasing patterns.
- Examined country-wise sales distribution.

Feature Engineering
- Created customer-level metrics.
- Generated features required for segmentation and CLV analysis.

SQL Analytics
- Performed business-focused analytical queries.
- Extracted customer, revenue, and product insights.

RFM Customer Segmentation
- Segmented customers based on:
  - Recency
  - Frequency
  - Monetary Value
- Identified high-value customer groups.

Customer Lifetime Value (CLV) Analysis
- Calculated customer lifetime value.
- Identified top revenue-generating customers.
- Measured customer contribution to overall revenue.

Customer Retention Analysis
- Performed cohort analysis.
- Measured retention rates across customer cohorts.
- Identified long-term customer behavior patterns.

Power BI Dashboard
Developed an interactive dashboard consisting of:

Revenue Overview
- Total Revenue
- Total Customers
- Total Orders
- Average Order Value
- Revenue Contribution by Country

Customer Segmentation Analysis
- RFM Segment Distribution
- High-Value Customer Analysis

CLV Analysis
- Customer Lifetime Value Metrics
- Top CLV Customers

Customer Retention Analysis
- Cohort Retention Heatmap
- Retention KPIs

Product Performance Analysis
- Top Products
- Revenue Distribution
- Product Insights

Business Insights

- Generated total revenue of approximately £8.74 million.
- Identified high-value customer segments through RFM analysis.
- Measured customer lifetime value to understand long-term profitability.
- Analyzed customer retention patterns using cohort analysis.
- Evaluated product performance and revenue contribution.
- Developed interactive dashboards for business decision-making.

Project Structure

data/
├── raw/
├── cleaned/

src/
├── data_inspection.py
├── data_cleaning.py
├── eda.py
├── feature_engineering.py
├── rfm_analysis.py
├── clv_prediction.py
├── cohort_analysis.py

sql/
├── customer_analytics_queries.sql

visualizations/
├── charts and analysis outputs

powerbi/
├── Online_Retail_Customer_Analytics.pbix

dashboard_screenshots/
├── Dashboard images

Author
Shiva Sai Tekumatla
