import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Function to set up the database table at the start
def init_db():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Call this function to make sure the table exists
init_db()

# API endpoint to get list of books
@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()
    book_list = [{'book_id': b[0], 'title': b[1], 'author': b[2], 'price': b[3]} for b in books]
    return jsonify(book_list)

# API endpoint to insert a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data['title']
    author = data['author']
    price = data['price']
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (title, author, price))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Book deleted successfully'}), 200


# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)