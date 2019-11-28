from flask_restful import Resource
from user.models import User
from database import db
from utils import db_util
from flask import request
import json


class UserView(Resource):
    # get方法
    def get(self):
        users = User.query.filter().all()
        return db_util.query_to_dict(users)

    # post方法
    def post(self):
        data = json.loads(request.data)
        user = User(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        db.session.add(user)
        return db_util.query_to_dict(user)
