from website import create_app, db
from website.models import User
from werkzeug.security import generate_password_hash

def create_admin():
    app = create_app()
    with app.app_context():
        existing_admin = User.query.filter_by(username='admin').first()
        
        if existing_admin:
            print('❌ Admin user already exists!')
            return
        
        admin = User(
            username='admin',
            email='admin@booktracker.com',
            first_name='Admin',
            last_name='User',
            password=generate_password_hash('admin123', method='pbkdf2:sha256'),
            role='admin'
        )
        
        db.session.add(admin)
        db.session.commit()
        
        print('Admin user created successfully!')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Username: admin')
        print('Password: admin123')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━')

if __name__ == '__main__':
    create_admin()