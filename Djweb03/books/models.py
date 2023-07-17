from django.db import models

"""

图书与人物表的关系为一对多：图书：人物 ==> 1：n
"""


# Create your models here.
# 定义图书模型类 book
class Book(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="图书名称")
    read = models.IntegerField(
        default=0,
        verbose_name="阅读量")
    comment = models.IntegerField(
        default=0,
        verbose_name="评论量")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '图书表'


# 定义人物类 Person
class Person(models.Model):
    GENDER_CHOICES = (
        (True, '男'),
        (False, '女')
    )

    name = models.CharField(
        max_length=10,
        verbose_name="人物姓名")
    gender = models.BooleanField(
        choices=GENDER_CHOICES,
        default=True,
        verbose_name="性别")
    book = models.ForeignKey(
        "Book",
        # on_delete的作用：当一个饮用的对象被删除时，Django将模拟 on_delete 参数所指定的 SQL 约束的行为
        # 常用的值：
        #   CASCADE：级联删除
        #       Django模拟了 SQL 约束 ON DELETE CASCADE 的行为，也删除了包含 ForeignKey 的对象
        #   PROTECT：防止删除被引用对象
        on_delete=models.CASCADE,
        verbose_name="所属图书")

    def __str__(self):
        return f"{self.name} ({self.get_gender_display()})"

    def get_gender_display(self):
        return '男' if self.gender else '女'

    class Meta:
        db_table = 'person'
        verbose_name = '人物表'


"""
模型类关联查询：
    1. 通过对象进行关联查询
        一到多：
            语法：对象.关联模型类名小写_set.all()
            Demo：查询 id 为 1 的书籍中所有的人物：
                book1 = Book.objects.get(id=1)
                book1.person_set.all()
        多到一：
            语法：多对应的模型类对象.一对应的模型类名小写
            Demo：查询 id 为 1 的人物所属的书籍：
                person1 = Person.objects.get(id=1)
                # 通过关联字段就可以直接获取到关联的数据对象
                book1 = person1.book
    
    2. 通过模型类进行关联查询
        一到多：
            语法：关联模型类名小写__关联模型类属性名__条件运算符=值
                如果没有 __条件运算符 表示等于
            Demo：查询图书，要求图书中人物的姓名包含 '蓉'
                list = Book.objects.filter(person__name__contains='蓉')
        多到一：
            语法：关联模型类名小写__关联模型类属性名__条件运算符=值
                如果没有 __条件运算符 表示等于
            Demo：查询人物，要求图书名为 '天龙八部' 中的所有人物
                plist = Person.objects.filter(book__title='天龙八部')


增删改操作：
    1. 添加数据
        通过模型类往数据库添加数据
        Demo：添加 神雕侠侣 书籍
            方式一：
                Book.objects.create(title='神雕侠侣', read=99, comment=23)
            方式二：
                obj = Book()
                obj.title = '连城诀'
                obj.read = 3450
                obj.comment = 534
                obj.save()
    2. 删除数据，使用 delete 方法
        通过模型类删除数据
        Demo：删除书名为 鹿鼎记 的书籍
            1. 查找要删除的对象
                obj = Book.objects.get(title='鹿鼎记')
            2. 调用 delete 方法
            obj.delete()
    3. 修改数据
        通过模型类修改数据
        Demo：修改书名为 神雕侠侣 的书籍
            1. 查询要修改的对象
                obj = Book.objects.get(title='倚天屠龙记')
            2. 通过属性直接修改字段的值
                obj.read = 999
            3. 调用 save 方法保存修改之后的结果
                obj.save()
        
            










"""
