import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"  # Use correct path if needed
df = pd.read_csv(file_path)

# Step 1: Clean and prepare the data
df_clean = df.dropna(subset=['Votes', 'Aggregate rating', 'Restaurant Name']).copy()
df_clean['Votes'] = pd.to_numeric(df_clean['Votes'], errors='coerce')

# Step 2: Find restaurants with highest and lowest number of votes
max_votes = df_clean['Votes'].max()
min_votes = df_clean['Votes'].min()

highest_voted = df_clean[df_clean['Votes'] == max_votes][['Restaurant Name', 'Votes', 'Aggregate rating']]
lowest_voted = df_clean[df_clean['Votes'] == min_votes][['Restaurant Name', 'Votes', 'Aggregate rating']]

print("🏆 Restaurants with the Highest Votes:")
print(highest_voted)

print("\n🪫 Restaurants with the Lowest Votes:")
print(lowest_voted)

# Step 3: Correlation between Votes and Rating
correlation = df_clean[['Votes', 'Aggregate rating']].corr().iloc[0, 1]
print(f"\n📊 Correlation between Votes and Aggregate Rating: {correlation:.2f}")

# Step 4: Plot relationship between Votes and Rating
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Votes', y='Aggregate rating', data=df_clean, alpha=0.5, color='darkblue')
plt.title("Votes vs Aggregate Rating")
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate Rating")
plt.grid(True)
plt.tight_layout()
plt.show()