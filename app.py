from movie import Movie
from user import User

user = User("Anthony")

my_movie = Movie("Terminator","Science Fiction",True)

user.movies.append(my_movie)

print(user.watched_movies())

