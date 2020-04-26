from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=1)
    name = db.Column(db.String(64), unique=True)
    hero_role_id = db.Column(db.Integer, db.ForeignKey('hero_roles.id'))
    created_at = db.Column(db.DateTime, deafult=datetime.now())

    def __repr__(self):
        return "<Hero %s>" % self.name
