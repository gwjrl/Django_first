from flask import Flask

from App.views import bp
from FlaskProject import config
from FlaskProject.config import envs
from FlaskProject.ext import init_ext
from FlaskProject.route import init_route


def create_app(env):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')

    # 注册蓝图
    app.register_blueprint(bp)

    # 加载环境配置
    app.config.from_object(envs.get(env))

    # 加载第三方插件
    init_ext(app)

    # 加载路由
    init_route(app)
    return app