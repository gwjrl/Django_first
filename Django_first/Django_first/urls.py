"""Django_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

# 导入内部的引用，进行URL调度文件，相当于路由，暴露出视图函数
# 当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外。
urlpatterns = [
    # Django2. 0中可以使用 re_path() 方法来兼容 1.x 版本中的 url() 方法，一些正则表达式的规则也可以通过 re_path() 来实现

    re_path(r'^book/', include('book.urls'), name ='index'),
    # path('book/', include('book.urls')),
    path('admin/', admin.site.urls),
]
