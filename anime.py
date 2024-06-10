import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv('anime_ratings.csv')

anime_ratings = df.pivot_table(index='user_id', columns='anime_title', values='rating')
anime_ratings = anime_ratings.fillna(0)

print('Pivot Table')
print(anime_ratings)

similarity_matrix = cosine_similarity(anime_ratings.T)

similarity_df = pd.DataFrame(similarity_matrix, index=anime_ratings.columns, columns=anime_ratings.columns)

print('\nCosine Similarity Matrix:')
print(similarity_df)

with open('anime_similarity.pkl', 'wb') as file:
    pickle.dump(similarity_df, file)

def get_recommendations(anime_title, similarity_df, n=1):
    if anime_title not in similarity_df.columns:
        return "Anime not found in the database"
    
    similar_animes = similarity_df[anime_title].sort_values(ascending=False)
    top_animes = similar_animes.index[1:n+1]

    return top_animes


print('\nRecommendations for One Piece')
print(get_recommendations('One Piece', similarity_df, n=1))