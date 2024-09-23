from flask import Blueprint
from .services import add_book_service, get_book_by_id_service, get_all_books_service, update_book_service, delete_book_by_id_service

books = Blueprint('books', __name__)

# add a new book
@books.route('/book-management/book', methods=['POST'])
def add_book():
    return add_book_service()

# get book by id
@books.route('/book-management/book/<int:id>', methods=['GET'])
def get_book(id):
    return get_book_by_id_service(id)

# get all books
@books.route('/book-management/books', methods=['GET'])
def get_all_books():
    return get_all_books_service()

# update book by id
@books.route('/book-management/book/<int:id>', methods=["PUT"])
def update_book_by_id(id):
    return update_book_service(id)

# delete book by id
@books.route('/book-management/book/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    return delete_book_by_id_service(id)