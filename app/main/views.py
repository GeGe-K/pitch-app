from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from . import main

# Views
@main.route('/')
def index():
    """
    Function that renders the index.html file
    """
    title = 'Welcome to pitches!'
    return render_template('index.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)


# @main.route('/pitch/comment')
# @login_required
# def new_comment():
#     pass