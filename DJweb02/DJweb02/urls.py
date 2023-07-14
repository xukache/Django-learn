from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    # 将应用中的 urls 文件包含进来
    re_path(r'^news/', include('news.urls'))
]
