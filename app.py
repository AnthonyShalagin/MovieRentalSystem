from movie import Movie
from user import User

user = User("Anthony")

user.add_movie("Terminator", "Sci-Fi", )
user.add_movie("Matrix", "Sci-Fi", )

user.save_to_file()

