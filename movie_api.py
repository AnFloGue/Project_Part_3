import requests

def fetch_movie_data(title):
    api_key = 'your_api_key'  # Replace with your actual OMDB API key
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return {
                'title': data['Title'],
                'year': data['Year'],
                'rating': data['imdbRating'],
                'genre': data['Genre']
            }
    return None