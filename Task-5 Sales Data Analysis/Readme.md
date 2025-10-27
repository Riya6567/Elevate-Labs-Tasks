# 🧠 Task 5: Data Analysis on CSV Files

## 📘 Objective
Analyze **sales data** using **Python** and **Pandas** to gain valuable insights and visualize sales performance trends.

---

## 🧰 Tools & Technologies
- **Python**
- **Pandas**
- **Matplotlib**
- **Jupyter Notebook / Google Colab**

---

## 📂 Dataset
**Source:** [Kaggle – Sample Sales Data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)  
**File:** `sales_data_sample.csv`
---

## ⚙️ Steps & Methodology

### 1. **Data Loading**
- Loaded the dataset using `pandas.read_csv()`
- Handled encoding issues with `encoding='latin1'`
- Displayed the first few records using `df.head()`

### 2. **Data Exploration**
- Checked dataset structure with `df.info()`
- Generated summary statistics with `df.describe()`
- Checked for missing values

### 3. **Data Analysis**
- Analyzed **total sales by product line**
- Analyzed **sales by country**
- Identified **top 10 customers by total sales**
- Examined **monthly sales trends**
- Computed **correlation matrix** for numeric fields

### 4. **Data Visualization**
Used **Matplotlib** to plot:
- Bar charts for sales by product line and country  
- Horizontal bar chart for top customers  
- Line chart for monthly sales trends  
- Heatmap for correlation matrix  

---

## 📊 Key Insights
- Certain **product lines** contribute significantly higher sales.  
- **Countries** such as USA and France dominate total revenue.  
- **Top customers** show major contribution to overall sales figures.  
- Monthly trends reveal **seasonal sales patterns**.
