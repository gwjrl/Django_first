# 定义api接口

from flask_restful import Api

from App.views import AppResource

from User.view import UsersResource

app_api =Api()
app_api.add_resource(AppResource, '/app/')

# 用户接口
user_api = Api(prefix='/users/')
# 第一个参数：视图函数名 第二个参数：路由的地址，以及string:todo_id代表传递的是一个字符串，且是必要参数
user_api.add_resource(UsersResource, '/')

