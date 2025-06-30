import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"  # Use raw string to avoid escape issues
df = pd.read_csv(file_path)

# 1. Analyze the distribution of aggregate ratings
rating_counts = df['Aggregate rating'].value_counts().sort_index()

# 2. Most common rating
most_common_rating = rating_counts.idxmax()
most_common_rating_count = rating_counts.max()

# 3. Average number of votes
average_votes = df['Votes'].mean()

# Plotting the rating distribution
plt.figure(figsize=(10, 5))
bars = plt.bar(rating_counts.index.astype(str), rating_counts.values, color='lightgreen')
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Aggregate Ratings")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 10, f'{height}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Display results
print(f"Most Common Rating: {most_common_rating} ({most_common_rating_count} restaurants)")
print(f"Average Number of Votes: {average_votes:.2f}")
