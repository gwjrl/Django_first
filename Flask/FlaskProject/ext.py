from flask_migrate import Migrate
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy

from Blog.fields_template import blog_fields

db = SQLAlchemy()

# 第三方库引用文件

migrate = Migrate()


# 参数请求解析
parser = reqparse.RequestParser()
parser.add_argument(blog_fields)   # 对fields资源模板进行参数解析


def init_ext(app):
    migrate.init_app(app, db)