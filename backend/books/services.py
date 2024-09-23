from backend.extension import db
from backend.library_ma import BookSchema
from backend.model import Books
from flask import request, jsonify
import json

# lay ra 1 quyen sach
book_schema = BookSchema()
# lay ra tat ca quyen sach
books_schema = BookSchema(many=True)

def add_book_service():
    data = request.json
    if data and ('name' in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data):
        name = request.json['name']
        page_count = request.json['page_count']
        author_id = request.json['author_id']
        category_id = request.json['category_id']

        try:
            new_book = Books(name,page_count,author_id,category_id)
            db.session.add(new_book)
            db.session.commit()
            return "Add success"
        except IndentationError:
            db.session.rollback()
            return "Can not add book"
    else:
        return "Request error!!!"
    
def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return "Not found"
    
def get_all_books_service():
    books = Books.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return "Not found"
    
def update_book_service(id):
    book = Books.query.get(id)
    data = request.json
    if book and 'page_count' in data:
        try:           
            book.page_count = data['page_count']
            db.session.commit()
            return "Book Updated"
        except IndentationError:
            db.session.rollback()
            return "Can not update book"
    else:
        return "Not found book"

def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "Book Deleted"
        except IndentationError:
            db.session.rollback()
            return "Can not delete book"
    else:
        return "Not found book"