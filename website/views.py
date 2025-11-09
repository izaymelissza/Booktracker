from flask import Blueprint, render_template
from flask_login import login_required, current_user
views = Blueprint('views', __name__)

@views.route('/home')
def home():
    return render_template("home.html", user=current_user)

@views.route('/books')
@login_required
def books():
    return "<p>Books</p>"

@views.route('/reading-lists')
@login_required
def reading_lists():
    return "<p>reading lists</p>"

@views.route('/stats')
@login_required
def stats():
    return "<p>Stats</p>"
