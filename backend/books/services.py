from backend.extension import db
from backend.library_ma import BookSchema
from backend.model import Books
from flask import request
import json

# lay ra 1 quyen sach
book_schema = BookSchema
# lay ra tat ca quyen sach
books_schema = BookSchema(many=True)

def add_book_service():
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