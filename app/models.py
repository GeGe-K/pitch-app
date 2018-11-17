from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    User model class to create users.

    Args:
        db.Model - connects our class to the database.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    @property
    def password(self):
        """
        Method that raises an error when a user tries to access the passwords.
        """
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        """
        Method that generates hashes for passwords.
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        Method that checks if the password hashes are the same.
        """
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        """
        Method used for debugging the database.
        """
        return f'User {self.username}'

class Pitch(db.Model):
    """
    Pitch model class to create pitches.

    Args:
        db.Model - connects our class to the database.
    """
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    users = db.relationship('User', backref = 'pitch', lazy = 'dynamic')

    def __repr__(self):
        """
        Method used for debugging the database.
        """
        return f'User {self.username}'
