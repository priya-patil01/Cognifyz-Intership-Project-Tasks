import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\\Users\\priya\\Downloads\\Dataset .csv"
df = pd.read_csv(file_path)

# Count number of restaurants in each price range
price_range_counts = df['Price range'].value_counts().sort_index()

# Calculate percentage of restaurants in each price range
total_restaurants = len(df)
price_range_percentages = (price_range_counts / total_restaurants) * 100

# Plotting the bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(price_range_counts.index.astype(str), price_range_percentages, color='skyblue')
plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants (%)")
plt.title("Distribution of Restaurants by Price Range")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add percentage labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Display percentages
print("Percentage of restaurants in each price range:")
print(price_range_percentages.round(2))
