# 创建数据模型
from django.db import models



class Book(models.Model):
    book = models.CharField(max_length=200)
    book_date = models.DateTimeField('date published')



