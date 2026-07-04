# ==========================================
# Customer Churn Prediction - Model Training
# Part 1: Import Libraries & Load Dataset
# ==========================================

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display shape of dataset
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==========================================
# Part 2: Data Cleaning
# ==========================================

# Drop customerID column (not useful for prediction)
df.drop("customerID", axis=1, inplace=True)

# Replace blank spaces in TotalCharges with NaN
df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])

# Check missing values
print("\nMissing Values After Conversion:")
print(df.isnull().sum())

# Remove rows with missing values
df.dropna(inplace=True)

# Verify dataset shape
print("\nDataset Shape After Cleaning:")
print(df.shape)

# Check data types
print("\nUpdated Data Types:")
print(df.dtypes)

# ==========================================
# Part 3: Exploratory Data Analysis (EDA)
# ==========================================

print("\nChurn Distribution:")
print(df["Churn"].value_counts())

plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.show()

numerical_features = ["tenure", "MonthlyCharges", "TotalCharges"]

for feature in numerical_features:
    plt.figure(figsize=(6,4))
    sns.histplot(df[feature], kde=True)
    plt.title(f"Distribution of {feature}")
    plt.show()


plt.figure(figsize=(8,5))
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=15)
plt.show()

plt.figure(figsize=(8,6))

sns.heatmap(
    df.select_dtypes(include=["int64","float64"]).corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()
