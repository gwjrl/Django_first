# 配置四大环境
def get_db_uri(db_info):
    database = db_info.get("DATABASE")
    driver = db_info.get('DRIVER')
    user = db_info.get('USER')
    password = db_info.get('PASSWORD')
    host = db_info.get('HOST')
    port = db_info.get('PORT')
    name = db_info.get('NAME')

    return "{}+{}://{}:{}@{}:{}/{}".format(database, driver, user, password, host, port, name)


class BaseConfig:
    DEBUG = False

    TESTING = False

    SECRET_KEY = "fghjklkjhvjhknlouibh3rwefjsdiojkre"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True

    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class TestingConfig(BaseConfig):
    TESTING = True

    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class StagingConfig(BaseConfig):
    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class OnLineConfig(BaseConfig):
    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "online": OnLineConfig,
    "default": OnLineConfig
}