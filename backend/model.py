from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from .extension import db

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        self.name = name

class Author(BaseModel):
    name = Column(String(50), nullable=False) 

    def __init__(self, name):
        self.name = name 
    
class Books(BaseModel):
    name = Column(String(100), nullable=False)
    page_count = Column(Integer)
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __init__(self, name, page_count, author_id, category_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id

class Students(BaseModel):
    name = Column(String(100), nullable=False)
    birth_date= Column(DateTime)
    gender = Column(String(10))
    class_name = Column(String(10))

    def __init__(self, name, birth_date, gender, class_name):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name
    
class Borrow(BaseModel):
    student_id = Column(Integer, ForeignKey(Students.id), nullable=False)
    book_id = Column(Integer, ForeignKey(Books.id), nullable=False)
    borrow_date = Column(DateTime, default = datetime.now())
    return_date = Column(DateTime)

    def __init__(self, student_id, book_id, borrow_date, return_date):
        self.student_id = student_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date
