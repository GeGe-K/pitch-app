from flask import render_template
from . import main

# Views
@main.route('/')
def index():
    """
    Function that renders the index.html file
    """
    title = 'Welcome to pitches!'
    return render_template('index.html', title = title)