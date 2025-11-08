from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/books')
def books():
    return "<p>Books</p>"

@auth.route('/reading-lists')
def reading_lists():
    return "<p>reading lists</p>"

@auth.route('/stats')
def stats():
    return "<p>Stats</p>"