class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched #Tells if the user has watched the movie


    def __repr__(self):
        return "<Movie {}>".format(self.name)


    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, json_data):
        return Movie(**json_data)   #argument unpacking, dictionary that you're passing as a set of named parameters
        #  same as:
        #  return Movie(name = json_data['name'], genre = json_data['genre'], watched = json_data['watched'])