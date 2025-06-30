import pandas as pd

# Load the dataset
file_path = "C:\\Users\\priya\\Downloads\\Dataset .csv"
df = pd.read_csv(file_path)

# 1. Identify the city with the highest number of restaurants
city_counts = df['City'].value_counts()
city_with_most_restaurants = city_counts.idxmax()
num_restaurants_in_top_city = city_counts.max()

# 2. Calculate the average rating for restaurants in each city
city_avg_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

# 3. Identify the city with the highest average rating
top_rated_city = city_avg_ratings.idxmax()
top_avg_rating = city_avg_ratings.max()

# Display results
print("City with the highest number of restaurants:")
print(f"{city_with_most_restaurants}: {num_restaurants_in_top_city} restaurants\n")

print("City with the highest average restaurant rating:")
print(f"{top_rated_city}: Average Rating {round(top_avg_rating, 2)}")
