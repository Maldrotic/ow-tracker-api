from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MapType(db.Model):
    __tablename__ = 'map_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    maps = db.relationship('Map', db.backref('map_type'))

    def __repr__(self):
        return "<MapType %s>" % self.name