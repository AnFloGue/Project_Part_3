import csv
import os
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'year', 'rating', 'poster'])

    def list_movies(self):
        movies = []
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies.append(row)
        return movies

    def add_movie(self, title, year, rating, poster):
        with open(self.file_path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([title, year, rating, poster])

    def delete_movie(self, title):
        movies = self.list_movies()
        movies = [movie for movie in movies if movie['title'] != title]
        with open(self.file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'year', 'rating', 'poster'])
            for movie in movies:
                writer.writerow([movie['title'], movie['year'], movie['rating'], movie['poster']])

    def update_movie(self, title, rating):
        movies = self.list_movies()
        for movie in movies:
            if movie['title'] == title:
                movie['rating'] = rating
                break
        with open(self.file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'year', 'rating', 'poster'])
            for movie in movies:
                writer.writerow([movie['title'], movie['year'], movie['rating'], movie['poster']])