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

# Average hsopital stay
avg_stay = df["Stay_Days"].mean()
print("\nAverage Hospital Stay: ", avg_stay)

# Age group Analysis, creates age groups using bins
df["Age_Group"] = pd.cut(df["Age"], bins=[0, 30, 50, 100], labels=["Young","Middle", "Senior"])
age_group_counts = df["Age_Group"].value_counts()
print("\nAge Group Distribution:")
print(age_group_counts)

# Visualization
# Bar chart for disease distribution
plt.figure()
disease_counts.plot(kind = 'bar')
# Title and labels
plt.title("Disease Distribution")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")
# Show chart
plt.show()

# Bar chart for age group distribution
plt.figure()
age_group_counts.plot(kind='bar')
plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.show()