from movie import Movie
from user import User
import json

user = User("Anthony")

user.add_movie("Matrix", "SciFi")
user.add_movie("Terminator", "SciFi")

with open('myfile.txt', 'w') as f:
    json.dump(user.json(), f)       #Dump user.json into f
