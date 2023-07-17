from django.urls import path, re_path, include
from .views import index, info, info2, user, user2

#  books 这个应用的路由规则
urlpatterns = [
    # http://127.0.0.1:8000/books/index/
    path('index/', index),
    path('info/', info),
    # http://127.0.0.1:8000/books/info/200
    re_path(r'info/(\d+)/', info2),
    # 位置参数传递：用小括号提取参数，小括号中写提取参数的正则表达式
    re_path(r'user/(.+?)/(.+?)/', user),
    # 关键字参数：用小括号提取参数，在小括号中使用 ?P<参数名> 给参数起名字
    re_path(r'user2/(?P<name>.+?)/(?P<pwd>.+?)/', user2),
]
