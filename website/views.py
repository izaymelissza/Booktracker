from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .decorators import admin_required
from .models import Book

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html", user=current_user)

@views.route('/books')
@login_required
def books():
    all_books = Book.query.order_by(Book.title).all()
    
    return render_template('books.html', books=all_books, user=current_user)

@views.route('/reading-lists')
@login_required
def reading_lists():
    return "<p>reading lists</p>"

@views.route('/stats')
@login_required
def stats():
    return "<p>Stats</p>"

@views.route('/admin/test')
@login_required
@admin_required
def admin_test():
    return "<h1>Welcome Admin!</h1><p>If you see this, the decorator works!</p>"

@views.route('/books/<int:book_id>')
@login_required
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    
    return render_template('book_detail.html', book=book, user=current_user)
