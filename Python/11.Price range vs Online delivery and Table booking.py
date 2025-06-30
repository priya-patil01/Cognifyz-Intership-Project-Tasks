import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"  # Update if needed
df = pd.read_csv(file_path)

# Step 1: Clean and prepare the relevant columns
df_clean = df[['Price range', 'Has Online delivery', 'Has Table booking']].dropna()

# Step 2: Convert 'Yes'/'No' to 1/0
df_clean['Has Online delivery'] = df_clean['Has Online delivery'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
df_clean['Has Table booking'] = df_clean['Has Table booking'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

# Step 3: Group by price range and calculate average availability
grouped = df_clean.groupby('Price range')[['Has Online delivery', 'Has Table booking']].mean().reset_index()

# Step 4: Print the table
print("📊 Average availability by Price Range:")
print(grouped)

# Step 5: Visualization
plt.figure(figsize=(10, 6))
sns.lineplot(data=grouped, x='Price range', y='Has Online delivery', marker='o', label='Online Delivery')
sns.lineplot(data=grouped, x='Price range', y='Has Table booking', marker='o', label='Table Booking')

plt.title("Availability of Online Delivery & Table Booking by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Proportion of Restaurants Offering Service")
plt.xticks(grouped['Price range'])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
