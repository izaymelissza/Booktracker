from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .decorators import admin_required
from .models import Book, Review
from . import db

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

@views.route('/books/<int:book_id>')
@login_required
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)

    reviews = Review.query.filter_by(book_id=book_id).order_by(Review.created_at.desc()).all()

    user_review = Review.query.filter_by(book_id=book_id, user_id=current_user.id).first()

    return render_template('book_detail.html', book=book,reviews=reviews, user_review=user_review, user=current_user)

@views.route('/books/create', methods=['GET', 'POST'])
@login_required
def create_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        genre = request.form.get('genre')
        publication_year = request.form.get('publication_year')
        pages = request.form.get('pages')
        description = request.form.get('description')
        cover_url = request.form.get('cover_url')
        
        if not title or len(title) < 1:
            flash('Title is required!', category='error')
        elif not author or len(author) < 1:
            flash('Author is required!', category='error')
        else:
            new_book = Book(
                title=title,
                author=author,
                isbn=isbn if isbn else None,
                genre=genre if genre else None,
                publication_year=int(publication_year) if publication_year else None,
                pages=int(pages) if pages else None,
                description=description if description else None,
                cover_url=cover_url if cover_url else None,
                created_by=current_user.id
            )
            
            db.session.add(new_book)
            db.session.commit()
            
            flash('Book added successfully!', category='success')
            return redirect(url_for('views.book_detail', book_id=new_book.id))
    
    return render_template('create_book.html', user=current_user)

@views.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)

    if current_user.role != 'admin' and book.created_by != current_user.id:
        flash('You can only edit your own books!', category='error')
        return redirect(url_for('views.book'))

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        genre = request.form.get('genre')
        publication_year = request.form.get('publication_year')
        pages = request.form.get('pages')
        description = request.form.get('description')
        cover_url = request.form.get('cover_url')

        if not title or len(title) < 1:
            flash('Title is required!', category='error')
        elif not author or len(author) < 1:
            flash('Author is required!', category='error')
        else:
            # Update a könyv adatait
            book.title = title
            book.author = author
            book.isbn = isbn if isbn else None
            book.genre = genre if genre else None
            book.publication_year = int(publication_year) if publication_year else None
            book.pages = int(pages) if pages else None
            book.description = description if description else None
            book.cover_url = cover_url if cover_url else None
            
            db.session.commit()
            
            flash('Book updated successfully!', category='success')
            return redirect(url_for('views.book_detail', book_id=book.id))
        

    return render_template('edit_book.html', book=book, user=current_user)

@views.route('/books/<int:book_id>/delete', methods=['POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    if current_user.role != 'admin' and book.created_by != current_user.id:
        flash('You can only delete your own books!', category='error')
        return redirect(url_for('views.books'))
    
    book.title = book.title

    db.session.delete(book)
    db.session.commit()

    flash(f"Book '{book.title}' deleted successfully!", category='success')
    return redirect(url_for('views.books'))

@views.route('/books/<int:book_id>/add-review', methods=['GET', 'POST'])
@login_required
def add_review(book_id):
    book = Book.query.get_or_404(book_id)

    existing_review = Review.query.filter_by(book_id=book_id, user_id=current_user.id).first()

    if existing_review:
        flash('You have already reviewed this book! You can edit your existing review.', category='error')
        return redirect(url_for('views.book_detail', book_id=book_id))
    
    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')

        if not rating:
            flash('Rating is required!', category='error')
        elif int(rating) < 1 or int(rating) > 5:
            flash('Rating must be between 1 and 5!', category='error')
        else:
            new_review = Review(
                user_id=current_user.id,
                book_id=book_id,
                rating=int(rating),
                comment=comment if comment else None
            )

            db.session.add(new_review)
            db.session.commit()

            flash('Review added successfully!', category='success')
            return redirect(url_for('views.book_detail', book_id=book_id))
        
    return render_template('add_review.html', book=book, user=current_user)

@views.route('/reviews/<int:review_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)

    if current_user.role != 'admin' and review.user_id != current_user.id:
        flash('You can only edit your own reviews!', category='error')
        return redirect(url_for('views.book_detail', book_id=review.book_id ))

    if request.method == 'POST':        
        rating = request.form.get('rating')
        comment = request.form.get('comment')

        if not rating:
            flash('Rating is required!', category='error')
        elif int(rating) < 1 or int(rating) > 5:
            flash('Rating must be between 1 and 5!', category='error')
        else:
            # Update a review adatait
            review.rating = int(rating)
            review.comment = comment
            
            db.session.commit()
            
            flash('Reviw updated successfully!', category='success')
            return redirect(url_for('views.book_detail', book_id=review.book_id))
        

    return render_template('edit_review.html', review=review, user=current_user)

@views.route('/reviews/<int:review_id>/delete', methods=['POST'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    
    # Ownership ellenőrzés: csak saját review-t vagy admin törölhet
    if current_user.role != 'admin' and review.user_id != current_user.id:
        flash('You can only delete your own reviews!', category='error')
        return redirect(url_for('views.book_detail', book_id=review.book_id))
    
    # Mentjük a book_id-t mert törlés után nem lesz review.book_id
    book_id = review.book_id
    
    # Törlés
    db.session.delete(review)
    db.session.commit()
    
    flash('Review deleted successfully!', category='success')
    return redirect(url_for('views.book_detail', book_id=book_id))

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