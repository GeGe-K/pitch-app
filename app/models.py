from . import db

class User(db.Model):
    """
    User model class to create users.

    Args:
        db.Model - connects our class to the database.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.Foreign_key('pitches.id'))

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
