from django.contrib import admin
from .models import NewsInfo, NewsType


# Register your models here.
# 定义 admin 的模型管理类
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'read', 'comment']


# 注册到 admin 后台
admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(NewsInfo, NewsInfoAdmin)
