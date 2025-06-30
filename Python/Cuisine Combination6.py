import pandas as pd
from collections import Counter
import itertools

# Load the dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"
df = pd.read_csv(file_path)

# Step 1: Drop missing values and make a safe copy
df_clean = df.dropna(subset=['Cuisines', 'Aggregate rating']).copy()

# Step 2: Break multi-cuisine strings into unique sorted cuisine pairs
pair_counter = Counter()
pair_ratings = {}

for _, row in df_clean.iterrows():
    cuisines = [c.strip() for c in row['Cuisines'].split(',')]
    rating = row['Aggregate rating']

    # Use only pairs if there are at least 2 cuisines
    if len(cuisines) >= 2:
        pairs = itertools.combinations(sorted(cuisines), 2)
        for pair in pairs:
            pair_counter[pair] += 1
            pair_ratings.setdefault(pair, []).append(rating)

# Step 3: Build results into a DataFrame
pair_data = []
for pair in pair_counter:
    count = pair_counter[pair]
    avg_rating = round(sum(pair_ratings[pair]) / len(pair_ratings[pair]), 2)
    pair_data.append({
        'Cuisine Pair': ' & '.join(pair),
        'Count': count,
        'Average Rating': avg_rating
    })

pair_df = pd.DataFrame(pair_data).sort_values(by='Count', ascending=False)

# Step 4: Show top 10 cuisine combinations
print("Top 10 Most Common Cuisine Pairs with Their Average Ratings:\n")
print(pair_df.head(10))
