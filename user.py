from movie import Movie


class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name,genre,False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

        #Filter takes in self.movie, stores it in movie, and compares whether movie.name is equal to the name passed in

        for movie in self.movies:
            if movie.name == name:
                self.movies.remove(self,name)

    def watched_movies(self):                                               #Get a list of movies that have been watched
        return list(filter(lambda movie: movie.watched, self.movies))       #Cast the filter to a list

    def save_to_file(self):                                                 #CSV format
        with open("{}.txt".format(self.name), "w") as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{}, {}, {}\n".format(movie.name, movie.genre, str(movie.watched)))

    @classmethod                         #Runs on the class itself
    def load_from_file(cls,filename):
        with open(filename, 'r') as f:
            content = f.readlines()      #load content
            username = content[0]        #extract username from first line
            movies = []
            for line in content[1:]:     #Start iterating from the first line
                movie_data = line.split(",")  #['name', 'genre', 'watched']                  #Extract name, genre, and watched parameter
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))  #Add to movies and check if watched

            user = cls(username)
            user.movies = movies
            return user








"""
    def watched_movies(self):             #Get a list of movies that have been watched
        watched_movies_list = []

        for movie in self.movies:
            if movie.watched:
                watched_movies_list.append(movie)

        return watched_movies_list
"""