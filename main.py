import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/patients.csv")

print("Dataset Preview: ")
print(df.head())

# Data Cleaning
df["Admission_Date"] = pd.to_datetime(df["Admission_Date"])
df["Discharge_Date"] = pd.to_datetime(df["Discharge_Date"])

# Find Number of stay days
df["Stay_Days"] = (df["Discharge_Date"] - df["Admission_Date"]).dt.days

print("\nData with Stay Days: ")
print(df)

# Analysis, most common diseases
# value_count() counts frequency of each disease
disease_counts = df["Disease"].value_counts()

print("\nMost Common Diseases:")
print(disease_counts)