from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# from DjangoUeditor.models import UEditorField  # 头部增加这行代码导入UEditorField


# Create your models here.
class Category(models.Model):
    '''类别表'''
    cname = models.CharField(verbose_name='类别名称', max_length=30, unique=True)  # unique=True 唯一

    class Meta:
        db_table = 't_category'  # 定义数据库表的名称
        verbose_name_plural = u'类别'  # 将admin后台的表名改成中文昵称

    # def __unicode__(self):
    #     return u'Category:%s'%self.cname
    def __str__(self):
        return self.cname


class Tag(models.Model):
    '''标签'''
    Tname = models.CharField(verbose_name='标签名称', max_length=30, unique=True)

    class Meta:
        db_table = 't_Tag'  # 定义数据库表的名称
        verbose_name_plural = u'标签'  # 将admin后台的表名改成中文昵称

    def __str__(self):
        return self.Tname


class Post(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    desc = models.CharField(verbose_name='简介', max_length=100)
    content = RichTextUploadingField(max_length=20480, verbose_name="帖子内容", null=True, blank=True)
    # content = body = UEditorField('内容', width=800, height=500,
    #                               toolbars="full", imagePath="upimg/", filePath="upfile/",
    #                               upload_settings={"imageMaxSize": 1204000},
    #                               settings={}, command=None, blank=True
    #                               )
    created = models.DateTimeField(verbose_name='创建时间', auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别')
    tag = models.ManyToManyField(Tag, verbose_name='标签')  # ManyToManyField 多对多

    class Meta:
        db_table = 't_post'  # 定义数据库表的名称
        verbose_name_plural = u'帖子'  # 将admin后台的表名改成中文昵称

    def __str__(self):
        return self.title
