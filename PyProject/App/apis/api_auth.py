
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from itsdangerous import Serializer, SignatureExpired, BadSignature

from FlaskProject.config import DevelopConfig
from User.model import BlogUser

auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized():
    error_info = '{}'.format('Invalid credentials')
    response = jsonify({'error': error_info})
    response.status_code = 403


    return response


def verify_password_for_token(username, password):

    # 验证输入的用户名和密码是否匹配

    user = BlogUser.query.filter_by(username=username).first()

    if user is None or not user.verify_password(password):
        # 结果不匹配
        return False

    return True


@auth.verify_password
def verify_password(username_or_token, password):
    user = verify_auth_token(username_or_token)
    if user is None:
        return verify_password_for_token(username_or_token, password)

    return user


def generator_auth_token(expiration=600):
    s = Serializer(secret_key=DevelopConfig.SECRET_KEY, expires_in=expiration)

    return s.dumps({'id': 1})


def verify_auth_token(token):
    s = Serializer(DevelopConfig.SECRET_KEY)

    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None

    user = BlogUser.query.get(data.get('id'))

    return user