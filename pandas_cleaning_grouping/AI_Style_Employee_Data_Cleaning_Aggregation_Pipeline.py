import pandas as pd
import numpy as np

# 🔹 Sample Data
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

# Detect missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing Salary values with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Drop Temporary_Notes column
df = df.drop(columns=["Temporary_Notes"])

# Rename Salary to Annual_Salary
df = df.rename(columns={"Salary": "Annual_Salary"})

# Group by Department
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

# Print final summary table
print("\nFinal Summary Table:")
print(summary)