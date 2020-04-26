from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HeroRole(db.Model):
    __tablename__ = 'hero_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    heroes = db.relationship('Hero', db.backref('hero_role'))

    def __repr__(self):
        return "<HeroRole %s>" % self.name
