from flask_restful import Resource

from app.models.user import User as UserModel


class User(Resource):

    def get(self):
        user = UserModel.query.get(1)
        return print(user)

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass