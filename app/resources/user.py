from flask_restful import Resource

from models.user import User as UserModel


class User(Resource):

    def get(self):
        UserModel.query

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass