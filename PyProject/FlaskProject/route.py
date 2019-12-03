from App.apis.api_main import user_api
from Blog.api import blog_api


def init_route(app):
    user_api.init_app(app)
    blog_api.init_app(app)


