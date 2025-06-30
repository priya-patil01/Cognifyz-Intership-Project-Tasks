import pandas as pd

# Load the dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"
df = pd.read_csv(file_path)

# Step 1: Clean the 'Has Online delivery' column (remove missing)
df_delivery = df.dropna(subset=['Has Online delivery', 'Aggregate rating']).copy()

# Normalize to lowercase for consistency (if needed)
df_delivery['Has Online delivery'] = df_delivery['Has Online delivery'].str.strip().str.lower()

# Step 2: Calculate percentage of restaurants offering online delivery
total = len(df_delivery)
online_yes = len(df_delivery[df_delivery['Has Online delivery'] == 'yes'])
online_delivery_percentage = round((online_yes / total) * 100, 2)

# Step 3: Compare average ratings
avg_rating_with_delivery = df_delivery[df_delivery['Has Online delivery'] == 'yes']['Aggregate rating'].mean()
avg_rating_without_delivery = df_delivery[df_delivery['Has Online delivery'] == 'no']['Aggregate rating'].mean()

# Output results
print(f"✅ Percentage of restaurants offering online delivery: {online_delivery_percentage}%\n")
print("📊 Average Ratings:")
print(f"With Online Delivery: {round(avg_rating_with_delivery, 2)}")
print(f"Without Online Delivery: {round(avg_rating_without_delivery, 2)}")
