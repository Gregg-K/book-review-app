from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from models.book import Book

book_bp = Blueprint("book", __name__)


@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()

    return jsonify([
        book.to_dict() for book in books
    ])


@book_bp.route("/books", methods=["POST"])
@jwt_required()
def create_book():
    data = request.get_json()

    user_id = int(get_jwt_identity())

    book = Book(
        title=data["title"],
        author=data["author"],
        description=data.get("description"),
        user_id=user_id
    )

    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 201


@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get_or_404(id)

    return jsonify(book.to_dict())


@book_bp.route("/books/<int:id>", methods=["PATCH"])
@jwt_required()
def update_book(id):
    book = Book.query.get_or_404(id)

    data = request.get_json()

    if "title" in data:
        book.title = data["title"]

    if "author" in data:
        book.author = data["author"]

    if "description" in data:
        book.description = data["description"]

    db.session.commit()

    return jsonify(book.to_dict())


@book_bp.route("/books/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_book(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        "message": "Book deleted successfully"
    })