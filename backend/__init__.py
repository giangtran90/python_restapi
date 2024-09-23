from flask import Flask, request, Blueprint
from .books.controller import books
from .extension import db, ma
from .model import Author, Category, Students, Books, Borrow
import os

def create_db(app):
   if not os.path.exists("backend/library.db"):
        with app.app_context():
            db.create_all()
        print("Created DB!")

# config_file = 'config.py' giup load file config len
def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    # dang ki mot blueprint(books)
    app.register_blueprint(books)
    # print(app.config['SECRET_KEY'])
    # print(app.config['SQLALCHEMY_DATABASE_URI'])
    
    return app