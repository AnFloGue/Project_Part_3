from storage_json import StorageJson

storage = StorageJson('movies.json')

# List movies
print(storage.list_movies())

# Add a movie
storage.add_movie('Inception', 2010, 8.8, 'inception_poster.jpg')
print(storage.list_movies())

# Update a movie
storage.update_movie('Inception', 9.0)
print(storage.list_movies())

# Delete a movie
storage.delete_movie('Inception')
print(storage.list_movies())