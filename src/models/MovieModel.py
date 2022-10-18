from database.db import getConnection
from .entities.Movie import Movie


class MovieModel():

    @classmethod
    def getMovies(self):
        try:
            connection = getConnection()

            movies = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM movies ORDER BY title ASC")
                resultset = cursor.fetchall()

            for row in resultset:
                movie = Movie(row[0], row[1], row[2], row[3])
                movies.append(movie.toJSON())

            connection.close()
            return movies

        except Exception as e:
            raise Exception(e)
