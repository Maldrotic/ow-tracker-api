from app import db


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='user_role')

    def __repr__(self):
        return "<UserRole %s>" % self.name
