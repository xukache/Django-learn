from django.urls import path
from .views import index, news_list, list2

# 配置路由规则
urlpatterns = [

    # http://域名(ip:端口)/news/index
    path('index', index),
    path('list', news_list),
    path('list2', list2),
]
