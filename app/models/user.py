from datetime import datetime

from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    # user_role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())

    # matches = db.relationship('Match', db.backref('user'))

    def __repr__(self):
        return '<User %s>' % self.username
