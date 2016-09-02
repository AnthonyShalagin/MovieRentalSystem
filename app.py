from movie import Movie
from user import User

user = User.load_from_file('Anthony.txt')

print(user.name)
print(user.movies)
