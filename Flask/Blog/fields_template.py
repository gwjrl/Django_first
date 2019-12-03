from flask_restful import fields, reqparse

# 对数据库数据进行参数解析
parser = reqparse.RequestParser
parser.add_argument('id', required=True)
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)
parser.add_argument('icon')
parser.add_argument('duration')

# 格式模板

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'icon': fields.String,
    'duration': fields.String
}