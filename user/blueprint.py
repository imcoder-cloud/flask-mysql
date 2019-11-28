# coding: utf8
from flask import Blueprint
from utils.blueprint_util import add_resource
from . import views

user_blueprint = Blueprint('user', __name__, url_prefix='/user')

config = [
    (views.UserView, '/')
]

add_resource(user_blueprint, config)
