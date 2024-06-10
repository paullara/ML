from flask import Flask, request, render_template
import pickle

with open('similarity_matrix.pkl', 'rb') as file:
    similarity_df = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('movie.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form['movie_title']

    if movie_title not in similarity_df.columns:
        return render_template('movie.html', recommendation_text='Movie not found in database')
    
    similar_movies = similarity_df[movie_title].sort_values(ascending=False)
    top_movies = similar_movies.index[1:6]

    recommendations = ', '.join(top_movies)

    return render_template('movie.html', recommendation_text=f'Recommended Movies: {recommendations}')

if __name__ == '__main__':
    app.run(debug=True)
