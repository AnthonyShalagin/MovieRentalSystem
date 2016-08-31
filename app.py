from movie import Movie
from user import User

my_movie = Movie("Terminator","Science Fiction")

user = User("Anthony")

user.movies.append(my_movie)

print(user)
print(user.movies)