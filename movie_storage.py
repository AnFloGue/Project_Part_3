import json

def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

def save_data(movies):
    with open('data.json', 'w') as file:
        json.dump(movies, file)

def add_movie(movies):
    name = input("\nNew movie to add: ")
    if name.lower() == 'q':
        return movies
    
    while True:
        try:
            year = int(input("\nPlease, enter the release year as integers (e.g., 2022): "))
            break
        except ValueError:
            print("Invalid input. Please enter a year as an integer (e.g., 2022): ")
    
    while True:
        try:
            rating = float(input("\nPlease, enter a value between 0-10: "))
            if 0 <= rating <= 10:
                break
            else:
                print("Invalid input. Please enter a value between 0 and 10: ")
        except ValueError:
            print("Invalid input. Please enter a numeric value: ")
    
    while name.lower() in movies.keys():
        print(f"\nMovie '{name}' already exists. ")
        name = input("Please enter a unique name: ")
    
    genre = input("\nEnter the movie genre (e.g., Comedy, Sci-Fi): ")
    
    movies[name] = {'rating': rating, 'year': year, 'genre': genre}
    
    save_data(movies)
    return movies

def delete_movie_by_name(movies):
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
        return movies
    
    name = input("\nPlease, enter name of the movie to delete: ").lower()
    
    for movie in movies.keys():
        if movie.lower() == name:
            del movies[movie]
            save_data(movies)
            print(f"\nMovie '{movie}' has been deleted.")
            return movies
    
    print(f"\nMovie not in the list")
    return movies

def update_movie(movies):
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
        return movies
    
    name = input("\nEnter name of the movie to update: ")
    
    if name in movies:
        while True:
            try:
                rating = float(input("\nPlease, enter a rating value between 0-10: "))
                if 0 <= rating <= 10:
                    movies[name]['rating'] = rating
                    break
                else:
                    print("Invalid input. Please enter a value between 0 and 10: ")
            except ValueError:
                print("Invalid input. Please enter a numeric value: ")
        
        while True:
            try:
                year = int(input("Enter new year of release (e.g., 2022): "))
                movies[name]['year'] = year
                break
            except ValueError:
                print("Invalid input. Please enter a year as an integer (e.g., 2022): ")
        
        update_genre = input("\nWould you like to update the genre (y/n)? ").lower()
        if update_genre == 'y':
            genre = input("Enter the new genre: ")
            movies[name]['genre'] = genre
        
        save_data(movies)
        return movies
    
    print(f"\nMovie not in the list")
    return movies