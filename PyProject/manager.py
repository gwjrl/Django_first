import os

from flask_migrate import MigrateCommand
from flask_script import Manager




# 获取系统环境
from FlaskProject import create_app

# env = os.environ.get('FLASK_PROJECT') or "default"
app = create_app("develop")

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
