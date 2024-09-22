from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .extension import db

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    name = Column(String(50), nullable=False)
    books = relationship('Books', backref='category', lazy=True)

    def __str__(self):
        return self.name 

class Author(BaseModel):
    name = Column(String(50), nullable=False) 
    books = relationship('Books', backref='author', lazy=True)

    def __str__(self):
        return self.name 
    
class Books(BaseModel):
    name = Column(String(100), nullable=False)
    page_count = Column(Integer)
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    borrow = relationship('Borrow', backref='books', lazy=True)

    def __str__(self):
        return self.name   

class Students(BaseModel):
    name = Column(String(100), nullable=False)
    birth_date= Column(DateTime)
    gender = Column(String(10))
    class_name = Column(String(10))
    borrow = relationship('Borrow', backref='students', lazy=True)

    def __str__(self):
        return self.name
    
class Borrow(BaseModel):
    student_id = Column(Integer, ForeignKey(Students.id), nullable=False)
    book_id = Column(Integer, ForeignKey(Books.id), nullable=False)
    borrow_date = Column(DateTime, default = datetime.now())
    return_date = Column(DateTime)
