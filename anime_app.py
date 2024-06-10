from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

with open('anime_similarity.pkl', 'rb') as file:
    similarity_df = pickle.load(file)


def get_recommendations(anime_title, similarity_df, n=1):
    if anime_title not in similarity_df.columns:
        return ["Anime not found"]
    
    similar_animes = similarity_df[anime_title].sort_values(ascending=False)
    top_animes = similar_animes.index[1:n+1]  # Exclude the anime itself

    return top_animes

@app.route('/')
def home():
    return render_template('anime.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    anime_title = request.form['anime_title']

    recommendations = get_recommendations(anime_title, similarity_df, n=1)

    return render_template('anime.html', recommendation_text=f'Recommended Anime: {", ".join(recommendations)}')

if __name__ == '__main__':
    app.run(debug=True)
