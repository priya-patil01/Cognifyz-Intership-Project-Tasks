import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"
df = pd.read_csv(file_path)

# Drop rows with missing cuisines or ratings
df = df.dropna(subset=['Cuisines', 'Aggregate rating', 'Votes'])

# Step 1: Clean and tokenize cuisine combinations
df['Cuisine List'] = df['Cuisines'].apply(lambda x: [c.strip() for c in str(x).split(',')])

# Step 2: Count cuisine frequencies
all_cuisines = [cuisine for sublist in df['Cuisine List'] for cuisine in sublist]
cuisine_counts = Counter(all_cuisines)

# Step 3: Average rating and total votes per cuisine
cuisine_stats = {}

for cuisine in cuisine_counts:
    mask = df['Cuisine List'].apply(lambda x: cuisine in x)
    subset = df[mask]
    avg_rating = subset['Aggregate rating'].mean()
    total_votes = subset['Votes'].astype(int).sum()
    cuisine_stats[cuisine] = {
        'Count': cuisine_counts[cuisine],
        'Average Rating': round(avg_rating, 2),
        'Total Votes': total_votes
    }

# Step 4: Convert to DataFrame for viewing
cuisine_df = pd.DataFrame.from_dict(cuisine_stats, orient='index')
cuisine_df = cuisine_df.sort_values(by='Count', ascending=False)

# Step 5: Show top 10 cuisines
print("🍽️ Top 10 Most Common Cuisines with Ratings and Popularity:\n")
print(cuisine_df.head(10))

# Step 6: Plot Top 10 Cuisines by Count
cuisine_df.head(10)['Count'].plot(kind='bar', color='orange', figsize=(10, 5), title='Top 10 Most Common Cuisines')
plt.ylabel("Number of Restaurants")
plt.xlabel("Cuisine")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
