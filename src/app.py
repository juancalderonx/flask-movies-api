from flask import Flask
from config import config

# Routes
from routes import Movie

app = Flask(__name__)

def pageNotFound(error):
    return '<h1>Not found page</h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Movie.main, url_prefix = '/api/movies')
    #Error handlers | Control de errores
    app.register_error_handler(404, pageNotFound)
    app.run()
