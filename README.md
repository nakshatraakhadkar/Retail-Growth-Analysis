# 🛒 Retail Growth Analysis: ETL Pipeline & RFM Segmentation

![Python](https://img.shields.io/badge/Python-3.11-blue) ![SQL](https://img.shields.io/badge/SQL-SQLite-orange) ![Pandas](https://img.shields.io/badge/Data-Pandas-green) ![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Executive Summary
**Business Problem:** A UK-based online retailer wants to identify high-value customer segments to optimize marketing budgets and reduce churn.  
**Solution:** Built an end-to-end data pipeline to ingest 500k+ transaction records, clean the data using Python, and perform an **RFM (Recency, Frequency, Monetary)** segmentation analysis.

**Key Impacts:**
* Identified **"Champion"** customers (top 5%) who drive significantly higher revenue than average users.
* Detected a seasonal sales spike in **November (Q4)**, advising inventory stocking strategies.
* Quantified a specific return rate on discounted items, highlighting quality control issues.

---

## 🛠️ Technical Architecture

### 1. Data Ingestion (ETL)
Instead of analyzing a static CSV, I simulated a production environment:
* **Extract:** Read raw `.xlsx` data (Online Retail II dataset) using `openpyxl`.
* **Transform:** Standardized column names and validated data types.
* **Load:** Built a **SQLite** database (`retail_db.sqlite`) to store the processed transactions, enabling SQL-based querying.

### 2. Data Cleaning & Preprocessing
* **Handling Nulls:** Removed rows with missing `Customer ID` (essential for customer segmentation).
* **Business Logic:** Separated "Returns" (Negative Quantity) from "Sales" into distinct datasets to prevent revenue calculation errors.
* **Feature Engineering:** Created a `TotalSales` metric (`Quantity` * `Price`) and parsed `InvoiceDate` for time-series analysis.

### 3. Customer Segmentation (RFM Analysis)
Used statistical quartiles to score customers from 1-5 on:
* **Recency:** Days since last purchase.
* **Frequency:** Total number of transactions.
* **Monetary:** Total revenue generated.

**Result:** Customers were labeled as *Champions*, *Loyal*, *Hibernating*, or *At Risk*.

---

## 📊 Visual Insights
*(Note: Visuals are generated in `visual.ipynb`)*

**1. Global Market Analysis:**
Identified that outside the UK, the highest revenue streams come from **EIRE (Ireland)**, **Germany**, and **France**, suggesting localized marketing campaigns for these regions.

**2. RFM Clusters:**
The scatter plot of Recency vs. Frequency reveals distinct clusters. "Champions" appear in the top-right (High Frequency, Low Recency), while "At Risk" customers drift to the bottom-right.

---

## 💻 How to Run This Project

**Prerequisites:**
* Python 3.x
* Git

**Step 1: Clone the Repository**
```bash
git clone [https://github.com/nakshatraakhadkar/Retail-Growth-Analysis.git](https://github.com/nakshatraakhadkar/Retail-Growth-Analysis.git)
cd Retail-Growth-Analysis
