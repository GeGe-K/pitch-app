from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from . import main
from .forms import UpdateProfile
from ..models import User
from .. import db


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

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)


# @main.route('/pitch/comment')
# @login_required
# def new_comment():
#     pass