import json
import os
from user import User


def menu():

    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter:\n 'a' to add a movie\n 'v' to view a list of movies\n "
             "'w' to set a movie as watched\n 'd' to delete a movie\n 'l' to see the list of watched movies\n"
             "' q' to save and quit\n")

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name\n")
            movie_genre = input("Enter the movie genre\n")
            user.add_movie(movie_name, movie_genre)

        elif user_input == 'v':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
                print("\n")

        elif user_input == 'w':
            movie_name = input("Enter the movie to set as watched\n")
            user.set_watched(movie_name )
            print("\n")


        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete:\n ")
            user.delete_movie(movie_name)

        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
                print("\n")


        elif user_input == 'f':
            with open(filename, "w") as f:
                json.dump(user.json(), f)           #dump user's json into f

        user_input = input("Enter:\n 'a' to add a movie\n 'v' to view a list of movies\n "
                 "'w' to set a movie as watched\n 'd' to delete a movie\n 'l' to see the list of watched movies\n"
                 "' f' to save and quit\n")

def file_exists(filename):
    return os.path.isfile(filename)

menu()