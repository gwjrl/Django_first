from flask import Blueprint
from flask_restful import Resource

bp = Blueprint('bp', __name__)


class AppResource(Resource):

    def get(self):
        return {'msg': 'app ok'}