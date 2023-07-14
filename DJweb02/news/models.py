from django.db import models

# Create your models here.
"""
新闻表（newsinfo）：
    ID 主键
    title 标题 （字符串）
    content 新闻内容 （大文本）
    b_date 新闻日期 （日期）
    read 阅读量 （整数）
模型类：必须继承 django.db.models.Model 类
"""


class NewsInfo(models.Model):
    """新闻表"""
    title = models.CharField(max_length=30)
    content = models.TextField()
    b_date = models.DateField()
    read = models.IntegerField()
