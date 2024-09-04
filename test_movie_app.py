from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def test_json_storage():
    print("Testing JSON Storage")
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()

def test_csv_storage():
    print("Testing CSV Storage")
    storage = StorageCsv('movies.csv')
    movie_app = MovieApp(storage)
    movie_app.run()

if __name__ == "__main__":
    test_json_storage()
    test_csv_storage()