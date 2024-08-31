import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 1, 2, 1, 2, 3, 4, 5],
    'movie_title': [
        'Toy Story', 'Jumanji', 'Grumpier Old Man',
        'Toy Story', 'Jumanji',
        'Jumanji', 'Grumpier Old Man',
        'Toy Story', 'Grumpier Old Man',
        'Toy Story', 'Grumpier Old Man',
        'Transformer', 'Avengers',
        'Toy Story', 'Avengers',
        'Avengers', 'Toy Story',
        'Avengers', 'Jumanji'
    ],
    'rating': [5, 3, 4, 4, 5, 2, 4, 5, 3, 4, 3, 3, 5, 4, 4, 4, 4, 4, 5]
}

df = pd.DataFrame(data)

#Create a pivot table   
movie_ratings = df.pivot_table(index='user_id', columns='movie_title', values='rating')

print(movie_ratings)

#Fill NaN values with 0
movie_ratings = movie_ratings.fillna(0)

#Calculate cosine similarity
similarity_matrix = cosine_similarity(movie_ratings.T)

#Convert to DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=movie_ratings.columns, columns=movie_ratings.columns)

with open('similarity_matrix.pkl', 'wb') as file:
    pickle.dump(similarity_df, file)
