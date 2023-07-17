from django.db import models

# Create your models here.
"""
# 新闻类型表：时尚杂志、国际新闻、体育新闻、时事政治、科技前沿。。。
    NewsType 表
        id: 主键
        name: 类型名称 字符串
        
# 新闻信息表：保存每一篇新闻的详细信息
    NewsInfo 表
        id: 主键
        title: 标题 字符串
        content: 内容 文本
        read: 阅读量 整数
        comment: 评论数量 整数
        
数据表之间的关系：
    一对一：OneToOneField: 一对一，将字段定义在任意一端中
    一对多：ForeignKey: 一对多，将字段定义在多的一端中
    多对多：ManyToManyField: 多对多，将字段定义在任意一段中
"""


class NewsType(models.Model):
    """定义新闻类型的模型类"""
    name = models.CharField(
        max_length=20,
        verbose_name='类型名称',
        help_text='类型名称')

    class Meta:
        # 默认生成的表名: 应用名_模型类名小写，可以在此处自己指定表名
        db_table = 'type'
        # 表的说明信息，在 django 后台中可以看到
        verbose_name = '新闻类型'

    # __str__ 方法的作用：可以设置更改对象显示出来的内容
    def __str__(self):
        return self.name


class NewsInfo(models.Model):
    """定义新闻信息的模型类"""
    title = models.CharField(
        max_length=100,
        verbose_name='标题',
        help_text='标题')

    content = models.TextField(
        verbose_name='新闻内容',
        help_text='新闻内容')

    read = models.IntegerField(
        verbose_name='阅读量',
        help_text='阅读量')

    comment = models.IntegerField(
        verbose_name='评论数量',
        help_text='评论数量')
    # 维护多对多关系
    type = models.ManyToManyField(
        'NewsType',
        verbose_name='新闻类型',
        help_text='新闻类型')

    class Meta:
        db_table = 'news'
        verbose_name = '新闻信息'

    def __str__(self):
        return self.title


"""
模型类的查询方法：
    get方法：查询一条数据
        Demo：查询 id 为 1 的数据
            NewsType.objects.get(id=3)
        特点：只能查询满足条件的唯一数据
            没有找到符合条件的数据，直接报错
            找到多条符合条件的，直接报错
            
    filter方法：根据条件过滤查询
        返回的值是一个 QuerySet 对象（查询集）
        Demo：查询 name 为 时尚杂志 的数据
            NewsType.objects.filter(name='时尚杂志')
        
    all方法：返回模块类对应的表中所有的数据
        返回的值是一个 QuerySet 对象（查询集）
        Demo：查询 NewsType 中的数据
            NewsType.objects.all()
        
    exclude方法：查询不符合条件的数据
        Demo：查询 name 不为 时尚杂志 的数据
            NewsType.objects.exclude(name='时尚杂志')
    
    order_by：排序的方法
        Demo：按照 read 排序新闻信息（默认）
                NewsInfo.objects.all().order_by('read')
        排序规则：
            默认升序
            降序排序（'-read'）

查询集：
    支持索引与切片取值
    支持再次调用查询的方法
    
模糊条件匹配查询：
    语法：字段名__条件 = 值
    1. contains：包含查询：
        Demo：查询新闻类型名称中包含‘新闻’这两个字的数据
            NewsType.objects.filter(name__contains='新闻')
    2. startswith：查询以xxx开头：
        Demo：查询以’体育‘开头的新闻类别
            NewsType.objects.filter(name__startswith='体育')
    3. endswith：查询以xxx结尾
        Demo：查询以’杂志‘结尾的新闻类别
            NewsType.objects.filter(name__endswith='杂志')

范围查询：
    4. in：查询某个范围内的数据
        Demo：查询 id 为 1 3 5 的数据
            NewsType.objects.filter(id__in=[1, 3, 5])

比较查询：
    5. gt：大于
        Demo：查询 id 大于等于 2 的数据
            NewsType.objects.filter(id__gte=2)
    6. lt：小于
    7. gte：大于等于
    8. lte：小于等于

空查询：
    9. isnull: 是否为空
        Demo：查询标题不为空的新闻
            NewsInfo.objects.filter(title__isnull=False)
            
F对象：用于比较查询数据的两个属性
    1. 导入：
        from django.db.models import F
    2. 查询
        Demo1：查询 阅读量 大于等于 评论数量 的新闻
            NewsInfo.objects.filter(read__gte=F('comment'))
        Demo2：查询 阅读量 大于等于 评论数量*2 的新闻
        NewsInfo.objects.filter(read__gte=F('comment')*2)
    3. 备注：F对象查询的结果可以直接进行算术运算
    
Q对象：用于逻辑查询（与或非）
    1. 导入：
            from django.db.models import Q
    2. 逻辑与(&)：多个条件同时成立
        不使用Q对象：
            Demo：查询阅读数量大于 40, 评论数量大于 35 的数据
                NewsInfo.objects.filter(read__gt=40,comment__gt=35)
        使用Q对象：
            Demo：查询阅读数量大于 40, 评论数量大于 35 的数据
                NewsInfo.objects.filter(Q(read__gt=40) & Q(comment__gt=35))
    3. 逻辑或(|)：多个条件符合一个即可    
        Demo：查询阅读数量大于 10, 或者评论数量大于 30 的数据
            NewsInfo.objects.filter(Q(read__gt=10) | Q(comment__gt=30))
    4. 逻辑非(~)：查询不符合条件的
        通过 exclude 方法查询(常用)：
            Demo：查询 id 不为 1 的数据
                NewsInfo.objects.exclude(id=1)
        通过Q对象查询：
            Demo：查询 id 不为 1 的数据
                NewsInfo.objects.filter(~Q(id=1))
   
聚合函数：sum avg max min count
    导入：
        from django.db.models import Sum, Avg, Max, Min, Count
    结合 aggregate 方法使用
    Max：
        Demo：查询评论数最高的数据
            NewsInfo.objects.aggregate(Max('comment'))
            
     
"""
