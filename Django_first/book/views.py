from django.http import HttpResponse


# 创建视图函数
from django.shortcuts import redirect, render


def index(request):
    contxt = {}
    contxt['hello'] = 'nihao'
    return render(request, 'index.html', contxt)
