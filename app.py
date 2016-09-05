from movie import Movie
from user import User
import json

with open('myfile.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json())
