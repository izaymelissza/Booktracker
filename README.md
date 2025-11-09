# 📚 BookTracker

Flask alkalmazás könyvek követésére, értékelésekkel és olvasási listákkal.

## Funkciók

- 🔐 Felhasználói autentikáció (Regisztráció, Bejelentkezés)
- 📖 Könyv (CRUD műveletek)
- ⭐ Értékelési rendszer (Csillagok + kommentek)
- 📋 Személyes olvasási lista (Státusz követés)

## Technológiák

- **Backend:** Flask, SQLAlchemy
- **Adatbázis:** SQLite
- **Autentikáció:** Flask-Login, Werkzeug
- **Frontend:** Bootstrap 4, Jinja2
- **Tervezett:** React integráció

## Telepítés
```bash
# Klónozás
git clone https://github.com/yourusername/booktracker.git
cd booktracker

# Függőségek telepítése
pip install -r requirements.txt

# Futtatás
python main.py
```

## Adatbázis séma

- **Users** - Felhasználók
- **Books** - Könyvek katalógusa
- **Reviews** - Értékelések
- **Reading_List** - Olvasási lista