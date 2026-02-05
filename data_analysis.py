
---



```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sample_data.csv")

print("Dataset Preview:")
print(df.head())

# -----------------------------
# Data Preprocessing
# -----------------------------
df.dropna(inplace=True)

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# Statistical Analysis
# -----------------------------
print("\nDescriptive Statistics:")
print(df.describe())

mean_sales = np.mean(df["Sales"])
median_sales = np.median(df["Sales"])
std_sales = np.std(df["Sales"])

print("\nStatistical Summary:")
print(f"Mean Sales: {mean_sales}")
print(f"Median Sales: {median_sales}")
print(f"Standard Deviation: {std_sales}")

# -----------------------------
# Data Visualization
# -----------------------------

# Line plot - Sales Trend
plt.figure()
plt.plot(df["Date"], df["Sales"])
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar chart - Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
plt.figure()
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Histogram - Sales Distribution
plt.figure()
plt.hist(df["Sales"], bins=10)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Box plot - Outlier Detection
plt.figure()
plt.boxplot(df["Sales"])
plt.title("Sales Outlier Analysis")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
