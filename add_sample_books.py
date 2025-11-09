from website import create_app, db
from website.models import User, Book

def add_sample_books():
    app = create_app()
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            print('Admin user not found! Create admin first.')
            return
        
        # Ellenőrizzük, vannak-e már könyvek
        existing_books = Book.query.count()
        if existing_books > 0:
            print(f'Database already has {existing_books} book(s).')
            answer = input('Add more books anyway? (yes/no): ')
            if answer.lower() != 'yes':
                return
        
        # Teszt könyvek
        sample_books = [
            {
                'title': '1984',
                'author': 'George Orwell',
                'isbn': '978-0-452-28423-4',
                'genre': 'Dystopian Fiction',
                'publication_year': 1949,
                'pages': 328,
                'description': 'A dystopian social science fiction novel and cautionary tale about the dangers of totalitarianism.',
                'cover_url': 'https://covers.openlibrary.org/b/isbn/9780452284234-L.jpg'
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'isbn': '978-0-06-112008-4',
                'genre': 'Southern Gothic',
                'publication_year': 1960,
                'pages': 324,
                'description': 'A novel about racial injustice and childhood innocence in the American South.',
                'cover_url': 'https://covers.openlibrary.org/b/isbn/9780061120084-L.jpg'
            },
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '978-0-7432-7356-5',
                'genre': 'Fiction',
                'publication_year': 1925,
                'pages': 180,
                'description': 'A story of decadence and excess exploring themes of idealism and social upheaval.',
                'cover_url': 'https://covers.openlibrary.org/b/isbn/9780743273565-L.jpg'
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'isbn': '978-0-14-143951-8',
                'genre': 'Romance',
                'publication_year': 1813,
                'pages': 432,
                'description': 'A romantic novel about manners, marriage, and morality in Georgian England.',
                'cover_url': 'https://covers.openlibrary.org/b/isbn/9780141439518-L.jpg'
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'isbn': '978-0-316-76948-0',
                'genre': 'Fiction',
                'publication_year': 1951,
                'pages': 234,
                'description': 'A story about teenage rebellion and alienation.',
                'cover_url': 'https://covers.openlibrary.org/b/isbn/9780316769488-L.jpg'
            }
        ]
        
        print('📚 Adding sample books...')
        for book_data in sample_books:
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                isbn=book_data['isbn'],
                genre=book_data['genre'],
                publication_year=book_data['publication_year'],
                pages=book_data['pages'],
                description=book_data['description'],
                cover_url=book_data['cover_url'],
                created_by=admin.id  # Admin hozta létre
            )
            db.session.add(book)
            print(f'  ✅ {book.title} by {book.author}')
        
        db.session.commit()
        
        print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(f'✅ Successfully added {len(sample_books)} books!')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━')

if __name__ == '__main__':
    add_sample_books()