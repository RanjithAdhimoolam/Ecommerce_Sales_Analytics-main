# 🛒 E-Commerce Sales Analytics Dashboard

This project is an interactive **E-Commerce Sales Analytics Dashboard** built using **Python and Streamlit**.

The main purpose of this project is to analyze e-commerce sales data and understand important business information such as sales, profit, customers, products, locations, and sales trends.

The dashboard allows users to apply filters and explore the data through interactive charts and tables.

---

## 📌 About the Project

Instead of manually analyzing a large sales dataset, this dashboard provides a simple way to understand the business performance.

Users can select different filters such as **date, region, state, category, product, payment method, sales channel, and order status**.

Based on the selected filters, all the numbers and charts in the dashboard are updated automatically.

---

## ✨ Features

### 📊 Sales Overview

The dashboard shows important KPIs such as:

- Total Revenue
- Total Profit
- Total Orders
- Total Quantity Sold
- Average Order Value
- Profit Margin
- Total Customers
- Average Customer Rating

### 📦 Product Analysis

This section helps understand product performance.

It includes:

- Top 10 products by revenue
- Top 10 products by profit
- Top products by quantity sold
- Product sales vs profit
- Detailed product information

### 👥 Customer Analysis

This section provides information about customers.

It includes:

- Top 10 customers
- Sales by customer segment
- Revenue by gender
- Sales by age group
- Customer details

### 🌍 Geographic Analysis

This section shows how sales are performing across different locations.

It includes:

- Sales by region
- Profit by region
- Top 15 states by sales
- City sales vs profit
- State summary

### 📈 Trends & Forecast

This section helps understand sales over time.

It includes:

- Monthly orders
- Monthly sales trends
- Monthly profit trends
- 3-month moving average
- 6-month sales forecast

The forecast uses a simple **linear trend approach** based on historical monthly sales.

---

## 🎛️ Interactive Filters

The dashboard provides filters in the sidebar:

- 📅 Date Range
- 🌍 Region
- 📍 State
- 🛍️ Category
- 🏷️ Product
- 💳 Payment Method
- 🛒 Sales Channel
- 📦 Order Status

There is also a **Reset Filters** button to return to the default view.

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Plotly**
- **HTML/CSS**

### Why these technologies?

- **Python** – Used for the overall development.
- **Pandas** – Used for data cleaning and analysis.
- **NumPy** – Used for calculations and sales forecasting.
- **Plotly** – Used to create interactive charts.
- **Streamlit** – Used to build the web dashboard.
- **HTML/CSS** – Used to customize the dashboard appearance.

### 📊 What This Project Can Help Answer

#### This dashboard can help answer questions like:

- Which products are generating the most sales?
- Which products are generating the most profit?
- Which cities and states have the highest sales?
- Which customer segment generates the most revenue?
- Which age group contributes the most sales?
- Which payment method is most commonly used?
- Which sales channel performs better?
- How are sales changing month by month?
- How is profit changing over time?
- What could sales look like over the next six months?

---

## 🧹 Data Preparation

Before analyzing the data, some basic cleaning and standardization is performed.

For example, similar product names are combined:

    Business Laptop → Laptop
    Gaming Laptop   → Laptop
    Smartphone      → Phone
    Budget Phone    → Phone

---

## 🔮 Sales Forecast

The dashboard includes a simple 6-month sales forecast.

The forecast is based on the historical monthly sales trend and uses a linear trend calculation.

It is mainly intended to give a basic idea of the possible future sales direction rather than being a highly advanced forecasting model.

---

## 📚 What I Learned

#### While working on this project, I learned and practiced:

- Python programming
- Pandas data analysis
- Data cleaning
- Data aggregation
- Exploratory data analysis
- KPI calculations
- Data visualization
- Plotly charts
- Streamlit dashboard development
- Interactive filters
- Customer analysis
- Product analysis
- Geographic analysis
- Time-based analysis
- Moving averages
- Basic sales forecasting

This project helped me understand how raw data can be converted into a useful business dashboard.

---

## 🚀 Future Improvements

#### I would like to improve this project in the future by adding:

- Year-over-Year sales analysis
- Month-over-Month growth
- More advanced forecasting models
- Customer retention analysis
- Repeat customer analysis
- More interactive filters
- Automated business insights
- PDF report generation
- Online deployment

---

## 📂 Project Structure

    E-Commerce-Sales-Analytics/
    │
    ├── app.py
    │
    ├── data/
    │   └── Ecommerce_Sales_Analytics_Dataset.csv
    │
    ├── assets/
    │   └── ecommerce_logo.png
    │
    ├── requirements.txt
    │
    └── README.md

---

## 👨‍💻 Author

RANJITH AATHIMOOLAM

Data Science / Data Analytics Enthusiast

This project was created as part of my practical learning and portfolio development in Python, Data Analytics, and Data Science.
