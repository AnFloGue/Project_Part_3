import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, filename):
        self.filename = filename

    def _load_data(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def list_movies(self):
        return self._load_data()

    def add_movie(self, title, year, rating, poster):
        movies = self._load_data()
        movies.append({'title': title, 'year': year, 'rating': rating, 'poster': poster})
        self._save_data(movies)

    def delete_movie(self, title):
        movies = self._load_data()
        movies = [movie for movie in movies if movie['title'] != title]
        self._save_data(movies)

    def update_movie(self, title, rating):
        movies = self._load_data()
        for movie in movies:
            if movie['title'] == title:
                movie['rating'] = rating
        self._save_data(movies)