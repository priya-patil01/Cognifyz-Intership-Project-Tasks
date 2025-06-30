import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"
df = pd.read_csv(file_path)

# Step 2: Make sure 'Reviews' and 'Aggregate rating' columns exist
review_col = 'Rating text'  # Change if your column is named differently

if review_col not in df.columns or 'Aggregate rating' not in df.columns:
    print(f"❌ Column '{review_col}' or 'Aggregate rating' not found.")
else:
    df_reviews = df.dropna(subset=[review_col, 'Aggregate rating']).copy()

    # Step 3: Clean and tokenize review text
    def clean_text(text):
        text = re.sub(r'[^a-zA-Z ]', '', str(text))  # Remove punctuation
        return text.lower().split()

    df_reviews['Tokens'] = df_reviews[review_col].apply(clean_text)

    # Step 4: Count all words
    all_words = [word for tokens in df_reviews['Tokens'] for word in tokens]
    word_freq = Counter(all_words)

    # Step 5: Define basic positive and negative word lists
    positive_words = {'good', 'great', 'excellent', 'tasty', 'amazing', 'nice', 'perfect', 'delicious', 'wonderful', 'love'}
    negative_words = {'bad', 'worst', 'awful', 'terrible', 'poor', 'disappointing', 'horrible', 'not', 'bland', 'slow'}

    # Step 6: Count positive and negative words
    positive_counts = {word: count for word, count in word_freq.items() if word in positive_words}
    negative_counts = {word: count for word, count in word_freq.items() if word in negative_words}

    # Step 7: Calculate review length
    df_reviews['Review Length'] = df_reviews[review_col].apply(lambda x: len(str(x).split()))
    avg_length = df_reviews['Review Length'].mean()

    # Step 8: Plot review length vs rating
    plt.figure(figsize=(8, 5))
    plt.scatter(df_reviews['Review Length'], df_reviews['Aggregate rating'], alpha=0.5, color='darkcyan')
    plt.title('Review Length vs Aggregate Rating')
    plt.xlabel('Review Length (word count)')
    plt.ylabel('Aggregate Rating')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Step 9: Output summary
    print("✅ Most Common Positive Words:")
    print(dict(sorted(positive_counts.items(), key=lambda x: x[1], reverse=True)))

    print("\n❌ Most Common Negative Words:")
    print(dict(sorted(negative_counts.items(), key=lambda x: x[1], reverse=True)))

    print(f"\n✍️ Average Review Length: {avg_length:.2f} words")
