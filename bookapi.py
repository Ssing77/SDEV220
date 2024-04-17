from flask import jsonify
from flask import Flask, request
app = Flask(__name__)
app.app_context().push()
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"
    


@app.route('/')
def index():
    return 'Hello world.'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}
        output.append(book_data)
    return {"book": output}

@app.route('/books/<id>')
def get_book(id):
    book = book.query.get_or_404(id)
    return jsonify({"book_name": book.book_name, "author": book.author, "publisher": book.publisher})

@app.route('/books', methods = ['post'])
def add_book():
    book = Book(name = request.json['book_name'], author = request.json['author'], publisher = request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books', methods = ['DELETE'])
def delete_book():
    book = book.query.get(id)
    if book is None:
        return {"error": "Not found'"}
    db.session.delete(book)
    return{"message": "Books"}