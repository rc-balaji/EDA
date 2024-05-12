import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

# Set up Faker
fake = Faker()

# Generate synthetic dataset
def generate_data(num_users=100, num_movies=50, num_ratings=1000):
    users = [{'user_id': i, 'name': fake.name()} for i in range(num_users)]
    movies = ['Movie {}'.format(i) for i in range(num_movies)]
    ratings = pd.DataFrame({
        'user_id': np.random.randint(0, num_users, num_ratings),
        'movie_name': np.random.choice(movies, num_ratings),
        'ratings': np.random.randint(1, 6, num_ratings)
    })
    users_df = pd.DataFrame(users)
    return pd.merge(ratings, users_df, on='user_id')

# Generate and load data
ratings_df = generate_data()

# EDA and Visualization
def explore_data(df):
    print(df.info())
    print(df.describe())

    # Ratings Distribution
    plt.figure(figsize=(8, 4))
    sns.countplot(x='ratings', data=df)
    plt.title('Distribution of Ratings')
    plt.show()

    # Top 10 Movies by Number of Ratings
    top_movies = df['movie_name'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_movies, y=top_movies.index, palette='deep')
    plt.title('Top 10 Movies by Number of Ratings')
    plt.xlabel('Number of Ratings')
    plt.show()

    # Average Rating per Movie
    avg_ratings = df.groupby('movie_name')['ratings'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    avg_ratings.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Movies by Average Ratings')
    plt.ylabel('Average Rating')
    plt.show()

    # Ratings Distribution for the Most Rated Movie
    most_rated_movie = df['movie_name'].value_counts().idxmax()
    movie_ratings = df[df['movie_name'] == most_rated_movie]['ratings']
    plt.figure(figsize=(8, 4))
    sns.countplot(x=movie_ratings, palette='viridis')
    plt.title(f'Ratings Distribution for {most_rated_movie}')
    plt.show()

# Call the function to explore data
explore_data(ratings_df)
