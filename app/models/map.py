from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Map(db.Model):
    __tablename__ = 'maps'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    map_type_id = db.Column(db.Integer, db.ForeignKey('map_types.id'))

    matches = db.relationship('Match', db.backref('map'))

    def __repr__(self):
        return "<Map %s>" % self.name