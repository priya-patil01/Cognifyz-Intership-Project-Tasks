import pandas as pd
from collections import Counter

# Load the dataset
file_path = "C:\\Users\\priya\\Downloads\\Dataset .csv" # Change path if needed
df = pd.read_csv(file_path)

# Drop rows with missing 'Cuisines' values
df_cuisine = df.dropna(subset=['Cuisines'])

# Count individual cuisines
cuisine_counter = Counter()
for entry in df_cuisine['Cuisines']:
    cuisines = [c.strip() for c in entry.split(',')]
    cuisine_counter.update(cuisines)

# Total number of restaurants
total_restaurants = len(df_cuisine)

# Top 3 most common cuisines with percentage
top_3_cuisines = cuisine_counter.most_common(3)
top_3_with_percentage = [
    (cuisine, count, round((count / total_restaurants) * 100, 2))
    for cuisine, count in top_3_cuisines
]

# Display results
print("Top 3 Most Common Cuisines and Their Percentages:")
for cuisine, count, percent in top_3_with_percentage:
    print(f"{cuisine}: {count} restaurants ({percent}%)")
