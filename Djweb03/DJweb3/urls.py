from django.contrib import admin
from django.urls import path, re_path, include

#  项目下的 urls.py 是整个项目路由匹配的入口
urlpatterns = [
    path('admin/', admin.site.urls),
    # 将应用中的 urls.py 的配置规则包含进去
    path('news/', include('news.urls')),
    path('books/', include('books.urls')),
]
