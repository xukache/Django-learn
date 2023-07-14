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
