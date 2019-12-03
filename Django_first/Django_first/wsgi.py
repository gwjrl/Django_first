"""
WSGI config for Django_first project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
# 运行在 WSGI 兼容的Web服务器上的入口文件
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_first.settings")

application = get_wsgi_application()
