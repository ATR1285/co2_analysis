import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Check if seaborn is installed
try:
    import seaborn as sns
except ImportError:
    print("Seaborn is not installed. Installing now...")
    os.system("pip install seaborn")
    import seaborn as sns

# Load Dataset
file_path = "synthetic_co2_emissions.csv"

if not os.path.exists(file_path):
    print(f"ERROR: File '{file_path}' not found! Make sure it exists in the current directory.")
    exit()

# Read the CSV file
df = pd.read_csv(file_path)

# Display first few rows
print("Dataset Preview:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Top 10 countries with highest CO₂ emissions
top_countries = df.sort_values(by="CO2_Emissions", ascending=False).head(10)

# Visualization - Top 10 Countries by CO2 Emissions
plt.figure(figsize=(12, 6))
sns.barplot(x="Country", y="CO2_Emissions", data=top_countries, palette="Reds_r")
plt.xticks(rotation=45)
plt.title("Top 10 Countries with Highest CO₂ Emissions")
plt.xlabel("Country")
plt.ylabel("CO₂ Emissions (Million Tons)")
plt.show()
