# 博客接口
from flask_restful import Api

from Blog.view import BlogsResource

blog_api = Api(prefix='/blog/')
blog_api.add_resource(BlogsResource, '/')