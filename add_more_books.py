from website import create_app, db
from website.models import Book, User

app = create_app()

books_data = [
    # Fiction
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "isbn": "978-0-06-088328-7", "genre": "Magical Realism", "year": 1967, "pages": 417, "description": "The multi-generational story of the Buendía family.", "cover": "https://covers.openlibrary.org/b/isbn/9780060883287-L.jpg"},
    
    # Science Fiction
    {"title": "Dune", "author": "Frank Herbert", "isbn": "978-0-441-17271-9", "genre": "Science Fiction", "year": 1965, "pages": 688, "description": "Epic science fiction about desert planet Arrakis.", "cover": "https://covers.openlibrary.org/b/isbn/9780441172719-L.jpg"},
    {"title": "Foundation", "author": "Isaac Asimov", "isbn": "978-0-553-29335-0", "genre": "Science Fiction", "year": 1951, "pages": 255, "description": "The collapse and rebirth of galactic civilization.", "cover": "https://covers.openlibrary.org/b/isbn/9780553293357-L.jpg"},
    {"title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "isbn": "978-0-441-00731-3", "genre": "Science Fiction", "year": 1969, "pages": 304, "description": "Gender and society on the planet Gethen.", "cover": "https://covers.openlibrary.org/b/isbn/9780441007318-L.jpg"},
    {"title": "Neuromancer", "author": "William Gibson", "isbn": "978-0-441-56956-6", "genre": "Cyberpunk", "year": 1984, "pages": 271, "description": "Groundbreaking cyberpunk novel.", "cover": "https://covers.openlibrary.org/b/isbn/9780441569595-L.jpg"},
    
    # Fantasy
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "isbn": "978-0-547-92822-7", "genre": "Fantasy", "year": 1937, "pages": 310, "description": "Bilbo Baggins' adventure to reclaim treasure from Smaug.", "cover": "https://covers.openlibrary.org/b/isbn/9780547928227-L.jpg"},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "isbn": "978-0-7564-0407-9", "genre": "Fantasy", "year": 2007, "pages": 662, "description": "Kvothe tells his life story.", "cover": "https://covers.openlibrary.org/b/isbn/9780756404079-L.jpg"},
    {"title": "A Game of Thrones", "author": "George R.R. Martin", "isbn": "978-0-553-10354-0", "genre": "Fantasy", "year": 1996, "pages": 694, "description": "The struggle for the Iron Throne begins.", "cover": "https://covers.openlibrary.org/b/isbn/9780553103540-L.jpg"},
    {"title": "The Way of Kings", "author": "Brandon Sanderson", "isbn": "978-0-7653-2635-5", "genre": "Fantasy", "year": 2010, "pages": 1007, "description": "Epic fantasy in the world of Roshar.", "cover": "https://covers.openlibrary.org/b/isbn/9780765326355-L.jpg"},
    
    # Mystery/Thriller
    {"title": "Gone Girl", "author": "Gillian Flynn", "isbn": "978-0-307-58836-4", "genre": "Thriller", "year": 2012, "pages": 415, "description": "A wife's disappearance and dark secrets.", "cover": "https://covers.openlibrary.org/b/isbn/9780307588364-L.jpg"},
    {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "isbn": "978-0-307-45454-7", "genre": "Mystery", "year": 2005, "pages": 465, "description": "Journalist and hacker investigate disappearance.", "cover": "https://covers.openlibrary.org/b/isbn/9780307454546-L.jpg"},
    {"title": "Big Little Lies", "author": "Liane Moriarty", "isbn": "978-0-399-16753-7", "genre": "Mystery", "year": 2014, "pages": 460, "description": "Secrets and lies in a beachside town.", "cover": "https://covers.openlibrary.org/b/isbn/9780399167539-L.jpg"},
    
    # Non-Fiction
    {"title": "Sapiens", "author": "Yuval Noah Harari", "isbn": "978-0-06-231609-7", "genre": "Non-Fiction", "year": 2011, "pages": 443, "description": "A brief history of humankind.", "cover": "https://covers.openlibrary.org/b/isbn/9780062316097-L.jpg"},
    {"title": "Educated", "author": "Tara Westover", "isbn": "978-0-399-59050-4", "genre": "Memoir", "year": 2018, "pages": 334, "description": "A memoir about education and family.", "cover": "https://covers.openlibrary.org/b/isbn/9780399590504-L.jpg"},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "isbn": "978-0-374-53355-7", "genre": "Psychology", "year": 2011, "pages": 499, "description": "How we think and make decisions.", "cover": "https://covers.openlibrary.org/b/isbn/9780374533557-L.jpg"},
    {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot", "isbn": "978-1-4000-5217-2", "genre": "Non-Fiction", "year": 2010, "pages": 381, "description": "The story of HeLa cells and medical ethics.", "cover": "https://covers.openlibrary.org/b/isbn/9781400052172-L.jpg"},
    
    # Classics
    {"title": "Moby-Dick", "author": "Herman Melville", "isbn": "978-0-14-243724-7", "genre": "Adventure", "year": 1851, "pages": 585, "description": "Captain Ahab's obsessive quest for the white whale.", "cover": "https://covers.openlibrary.org/b/isbn/9780142437247-L.jpg"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "isbn": "978-0-14-144114-6", "genre": "Romance", "year": 1847, "pages": 532, "description": "The story of an orphaned governess and her love.", "cover": "https://covers.openlibrary.org/b/isbn/9780141441146-L.jpg"},
    {"title": "Wuthering Heights", "author": "Emily Brontë", "isbn": "978-0-14-143955-6", "genre": "Gothic Fiction", "year": 1847, "pages": 416, "description": "Passion and revenge on the Yorkshire moors.", "cover": "https://covers.openlibrary.org/b/isbn/9780141439556-L.jpg"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "isbn": "978-0-14-044913-0", "genre": "Philosophical Fiction", "year": 1866, "pages": 671, "description": "Raskolnikov's moral dilemma after murder.", "cover": "https://covers.openlibrary.org/b/isbn/9780140449136-L.jpg"},
    
    # Contemporary
    {"title": "The Kite Runner", "author": "Khaled Hosseini", "isbn": "978-1-59448-000-3", "genre": "Historical Fiction", "year": 2003, "pages": 371, "description": "Friendship and redemption in Afghanistan.", "cover": "https://covers.openlibrary.org/b/isbn/9781594480003-L.jpg"},
    {"title": "Life of Pi", "author": "Yann Martel", "isbn": "978-0-15-100811-7", "genre": "Adventure", "year": 2001, "pages": 319, "description": "A boy, a tiger, and survival at sea.", "cover": "https://covers.openlibrary.org/b/isbn/9780156027328-L.jpg"},
    {"title": "The Book Thief", "author": "Markus Zusak", "isbn": "978-0-375-84220-7", "genre": "Historical Fiction", "year": 2005, "pages": 552, "description": "Death narrates a girl's story in Nazi Germany.", "cover": "https://covers.openlibrary.org/b/isbn/9780375842207-L.jpg"},
]

with app.app_context():
    # Find admin user
    admin = User.query.filter_by(role='admin').first()
    
    if not admin:
        print("❌ No admin user found! Run create_admin.py first.")
        exit()
    
    print(f"Adding books as user: {admin.username}")
    
    added_count = 0
    skipped_count = 0
    
    for book_info in books_data:
        # Check if book already exists
        existing = Book.query.filter_by(title=book_info['title']).first()
        
        if existing:
            print(f"⏭️  Skipped (exists): {book_info['title']}")
            skipped_count += 1
            continue
        
        book = Book(
            title=book_info['title'],
            author=book_info['author'],
            isbn=book_info['isbn'],
            genre=book_info['genre'],
            publication_year=book_info['year'],
            pages=book_info['pages'],
            description=book_info['description'],
            cover_url=book_info['cover'],
            created_by=admin.id
        )
        
        db.session.add(book)
        print(f"✅ Added: {book_info['title']} by {book_info['author']}")
        added_count += 1
    
    db.session.commit()
    print(f"\n🎉 Done! Added {added_count} books, skipped {skipped_count}.")