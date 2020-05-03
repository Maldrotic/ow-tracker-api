from datetime import datetime

from app import db


class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    map_id = db.Column(db.Integer, db.ForeignKey('maps.id'))

    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return "<Match %s>" % self.id
