from .extension import ma

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'birth_date', 'gender', 'class_name')

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'page_count', 'author_id', 'category_id')

class BorrowSchema(ma.Schema):
    class Meta:
        fields = ('id', 'student_id', 'book_id', 'borrow_date', 'return_date')