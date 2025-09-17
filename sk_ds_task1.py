# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/hydra/Downloads/population.csv")

print("Dataset Head:")
print(df.head(), "\n")

print("Summary Statistics:")
print(df.describe(include="all"), "\n")

print("Gender Distribution:")
if "Gender" in df.columns:
    print(df['Gender'].value_counts(), "\n")

if "Gender" in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="Gender", palette="Set2")
    plt.title("Gender Distribution in Population Dataset")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()

if "Age" in df.columns:
    plt.figure(figsize=(6,4))
    sns.histplot(data=df, x="Age", bins=10, kde=True, color="skyblue")
    plt.title("Age Distribution in Population Dataset")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

if "Age" in df.columns and "Gender" in df.columns:
    plt.figure(figsize=(6,4))
    sns.barplot(data=df, x="Gender", y="Age", palette="pastel")
    plt.title("Average Age by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Age")
    plt.show()
