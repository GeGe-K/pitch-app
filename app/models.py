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

    def __repr__(self):
        """
        Method used for debugging the database.
        """
        return f'User {self.username}'