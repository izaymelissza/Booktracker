from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user


def admin_required(f):
    """
    Decorator to require admin role for a route.
    Use after @login_required.
    
    Example:
        @app.route('/admin/users')
        @login_required
        @admin_required
        def manage_users():
            # Only admins can access this
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user is authenticated (should be caught by @login_required, but just in case)
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', category='error')
            return redirect(url_for('auth.login'))
        
        # Check if user has admin role
        if current_user.role != 'admin':
            flash('You do not have permission to access this page. Admin access required.', category='error')
            return redirect(url_for('views.home'))
        
        # If everything is OK, call the original function
        return f(*args, **kwargs)
    
    return decorated_function