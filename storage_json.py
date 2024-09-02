import os
import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def list_movies(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies.append({'title': title, 'year': year, 'rating': rating, 'poster': poster})
        with open(self.file_path, 'w') as file:
            json.dump(movies, file)

    def delete_movie(self, title):
        movies = self.list_movies()
        movies = [movie for movie in movies if movie['title'] != title]
        with open(self.file_path, 'w') as file:
            json.dump(movies, file)

    def update_movie(self, title, rating):
        movies = self.list_movies()
        for movie in movies:
            if movie['title'] == title:
                movie['rating'] = rating
                break
        with open(self.file_path, 'w') as file:
            json.dump(movies, file)