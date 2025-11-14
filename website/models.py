from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True)
    author = db.Column(db.String(150))
    isbn = db.Column(db.String(20))
    genre = db.Column(db.String(150))
    publication_year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    description = db.Column(db.Text)
    cover_url = db.Column(db.String(300))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))  # 1:N relationship with User
    
    # Relationships
    reading_lists = db.relationship('Reading_List', backref='book', lazy=True, cascade='all, delete-orphan')
    reviews = db.relationship('Review', backref='book', lazy=True, cascade='all, delete-orphan')

class Reading_List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    status = db.Column(db.Enum('TO_READ', 'READING', 'READ'), default='TO_READ')
    added_at = db.Column(db.Date(), nullable=True)
    started_reading_at = db.Column(db.Date(), nullable=True)
    finished_reading_at = db.Column(db.Date(), nullable=True)
    
    # Ensure a user can't add the same book twice to their reading list
    __table_args__ = (db.UniqueConstraint('user_id', 'book_id', name='_user_book_uc'),)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    comment = db.Column(db.Text, nullable=True)  # Optional text review
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())
    
    # Ensure a user can only review a book once
    __table_args__ = (db.UniqueConstraint('user_id', 'book_id', name='_user_book_review_uc'),)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.Enum('user', 'admin'), default='user')
    registration_date = db.Column(db.DateTime(timezone=True), default=func.now())

    books_created = db.relationship('Book', backref='creator', lazy=True)
    reading_lists = db.relationship('Reading_List', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

    