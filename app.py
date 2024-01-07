from flask import Flask, request, jsonify
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "tujestwpisanykod"

@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify(books.all())

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id - 1)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    books.create(data)
    books.save_all()
    return jsonify({"message": "Book created successfully"})

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    if books.get(book_id - 1):
        books.update(book_id - 1, data)
        books.save_all()
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    if books.get(book_id - 1):
        del books.books[book_id - 1]
        books.save_all()
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)