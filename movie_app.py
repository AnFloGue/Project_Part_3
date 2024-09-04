import requests
import subprocess
from storage_json import StorageJson

class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        for movie in movies:
            print(f"{movie['title']}: {movie}")

    def _command_add_movie(self):
        title = input("Enter movie title: ")
        api_key = '4a1990ae'
        response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey={api_key}')
        if response.status_code == 200:
            movie_data = response.json()
            if movie_data['Response'] == 'True':
                title = movie_data['Title']
                year = int(movie_data['Year'])
                rating = float(movie_data['imdbRating'])
                poster = movie_data['Poster']
                self._storage.add_movie(title, year, rating, poster)
                print(f"Movie '{title}' added successfully.")
            else:
                print(f"Movie not found: {movie_data['Error']}")
        else:
            print("Error fetching movie data")

    def _command_delete_movie(self):
        title = input("Enter movie title to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        title = input("Enter movie title to update: ")
        rating = float(input("Enter new rating: "))
        self._storage.update_movie(title, rating)

    def _command_movie_stats(self):
        movies = self._storage.list_movies()
        # Calculate and print statistics
        print("Statistics not implemented yet.")

    def _generate_website(self):
        print("Starting Flask server...")
        subprocess.run(["python", "app.py"])

    def run(self):
        try:
            while True:
                print("\nMenu:")
                print("1. List movies")
                print("2. Add movie")
                print("3. Delete movie")
                print("4. Update movie")
                print("5. Movie statistics")
                print("6. Generate website")
                print("7. Exit")
                choice = input("Enter choice: ")

                if choice == '1':
                    self._command_list_movies()
                elif choice == '2':
                    self._command_add_movie()
                elif choice == '3':
                    self._command_delete_movie()
                elif choice == '4':
                    self._command_update_movie()
                elif choice == '5':
                    self._command_movie_stats()
                elif choice == '6':
                    self._generate_website()
                elif choice == '7':
                    print(f"\nGoodbye, Thanks for visiting")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting the application.")

if __name__ == "__main__":
    storage = StorageJson('movies.json')
    app = MovieApp(storage)
    app.run()