from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, migrate, jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from models import User, Book, Review, Category, BookCategory

    from routes.auth import auth_bp
    from routes.book import book_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(book_bp)

    @app.route("/")
    def home():
        return {"message": "Book Review API is running"}

    return app


app = create_app()