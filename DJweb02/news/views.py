from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsInfo

# Create your views here.
"""
视图函数定义的基本要求
    1. 视图函数必须定义一个参数（通过命名为 request）
        request参数：用来接受客户端的请求信息的
    2. 视图函数的返回值必须是一个 HttpResponse 的对象（或者 HttpResponse 的子类对象）

视图使用的流程：
    1. 在应用的 views.py 定义视图函数
    2. 配置路由
        1) 在项目目录的 urls.py 中关联应用下的 urls.py 
            re_path(r'^news/', include('news.urls'))
        2) 在应用的目录下定义一个 urls.py 文件（可以直接 copy 项目目录下的 urls.py）
        3) 配置具体的访问规则
            ```from django.urls import path
            from .views import index
            
            # 配置路由规则
            urlpatterns = [
            
                # http://域名(ip:端口)/news/index
                path('index', index),
            ]```
"""

def index(request):
    res = 'index'
    return HttpResponse(res)

def news_list(request):
    """返回新闻列表"""
    # 获取 newsinfo 这个表中的所有数据
    # select * from newsinfo
    data = NewsInfo.objects.all()

    result = ''
    for item in data:
        title = f'<h1>{item.title}</h1>'
        result += title
    return HttpResponse(result)

"""
模板的配置和使用步骤：
    1. 在项目目录下创建一个 templates 文件夹
    2. 在 setting.py 中 TEMPLATES 选项中配置项目模板的根路径
        'DIRS': [BASE_DIR / 'templates'], 
    3. 在 templates 中创建和应用同名的文件夹
    4. 在 templates 下应用同名的文件夹中创建 html 模板页面
    5. 在 views.py 中定义视图函数，并返回 html 模板页面
    6. 配置路由访问规则
"""

# 在视图中使用模板文件
def list2(request):
    """返回模板的视图"""
    # 1. 通过模型去查询数据
    data = NewsInfo.objects.all()
    # 获取查询到的第一条新闻信息
    item = data[0]
    info = {
        "title": item.title,
        "content": item.content,
        "b_date": item.b_date,
        "read": item.read,
    }
    # render 渲染模板所需的三个参数：
    # 请求对象 request
    # 模板的路径 "news/list.html"
    # 要渲染到模板中的数据（必须是字典格式）
    return render(request, "news/list.html", info)
