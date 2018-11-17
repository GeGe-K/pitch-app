from flask import render_template
from . import auth

@auth.route('/login')
def login():
    """
    Function that renders the login html page.
    """
    return render_template('auth/login.html')
