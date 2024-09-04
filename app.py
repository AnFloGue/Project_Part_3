from flask import Flask, render_template, request, redirect, url_for
from storage_json import StorageJson
import requests

app = Flask(__name__)
storage = StorageJson('movies.json')  # or StorageCsv('movies.csv')

@app.route('/')
def index():
    movies = storage.list_movies()
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        api_key = 'your_api_key'  # Replace with your actual API key
        response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey={api_key}')
        if response.status_code == 200:
            movie_data = response.json()
            if movie_data['Response'] == 'True':
                title = movie_data['Title']
                year = int(movie_data['Year'])
                rating = float(movie_data['imdbRating'])
                poster = movie_data['Poster']
                storage.add_movie(title, year, rating, poster)
                return redirect(url_for('index'))
            else:
                return f"Movie not found: {movie_data['Error']}", 404
        else:
            return "Error fetching movie data", 500
    return render_template('add_movie.html')

if __name__ == '__main__':
    app.run(debug=True)