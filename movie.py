class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched #Tells if the user has watched the movie


    def __repr__(self):
        return "<Movie {}>".format(self.name)


