from flask import Flask, request, Blueprint
from .books.controller import books

# config_file = 'config.py' giup load file config len
def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    # dang ki mot blueprint(books)
    app.register_blueprint(books)
    print(app.config['SECRET_KEY'])
    return app