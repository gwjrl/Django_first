from flask import request, jsonify
from flask_restful import Resource, abort, marshal

from Blog.fields_template import user_fields
from .model import BlogUser


# 定义一个请求提示类
class Common(Resource):

    # 定义一个请求成功返回提示的函数
    def return_true_json(self, data, msg='请求成功'):
        return jsonify({
            'status': 1,
            'data': data,
            'msg': msg
        })


    def return_false_json(self, data=None, msg='请求失败'):
        return jsonify({
            'status': 0,
            'data': data,
            'msg': msg
        })

# 资源列表
# 通过类定义视图函数, 单一资源
class UsersResource(Resource):
    # 查询数据，用于更新，输出
    def get(self, user_id):
        user = BlogUser.query.filter_by(id=user_id).first()

        if user is None:
            abort(410, mag='找不到数据', data=None, status=0)
        else:
            return Common.return_true_json(Common, marshal(user, user_fields))


    # 用于插入数据
    def post(self, user_id):
        # 获取form表单中键值为data的参数
        user_fields[user_id] = request.form['data']
        return {user_id: user_fields[user_id]}

