from django.contrib import admin
from .models import NewsInfo

# Register your models here.
# 方式一：直接注册模型类，在后台 admin 显示的模型类的对象
# admin.site.register(NewsInfo)


# 方式二：自定义在 admin 后台显示的模型类字段
class NewsInfoAdmin(admin.ModelAdmin):
    # 通过 list_display 制定在后台显示的字段
    list_display = ['id', 'title', 'b_date', 'read']


# 将自定义数据展示的模型类，注册到后台系统中
admin.site.register(NewsInfo, NewsInfoAdmin)
