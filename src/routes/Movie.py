from flask import Blueprint, jsonify

# Models
from models.MovieModel import MovieModel

main = Blueprint('movieBlueprint', __name__)

@main.route('/')
def getMovies():
    try:
        movies = MovieModel.getMovies()
        return jsonify(movies)
    except Exception as e:
        return jsonify({"error": str(e)}),500