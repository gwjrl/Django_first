from werkzeug.security import generate_password_hash, check_password_hash

from FlaskProject.ext import db


class BlogUser(db.Model):
    # 博客用户
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    _password = db.Column('password', db.String(256), nullable=False)
    icon = db.Column(db.String(128), nullable=True)
    duration = db.Column(db.String(256), nullable=True)

    @property
    def password(self):
        raise AttributeError('密码不能被读取')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    # 校验
    def verify_password(self, password):  # 验证密码方法
        return check_password_hash(password, self._password)

    def __repr__(self):
        return "<User {}>".format(self.username)



    @staticmethod
    def register(username, password, icon, duration):
        user = BlogUser()
        user.username = username
        user.password = password
        user.icon = icon
        user.duration = duration
        db.session.add(user)
        db.session.commit()