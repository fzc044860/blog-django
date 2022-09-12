#coding=utf-8
from post.models import Post
from django.db.models import Count

def getRightInfo(request):
    #1、获取分类信息
    r_catepost = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')
    #2、近期文章
    r_recpost = Post.objects.all().order_by('-created')[:3]  #显示前三条
    #获取日期归档信息（使用原生查询 ）
    from django.db import connection
    cursor = connection.cursor()
    sql = "select created,count(*) from t_post GROUP BY DATE_FORMAT(created,'%Y-%m');"
    cursor.execute(sql)
    r_filepost = cursor.fetchall()  #归档后的数据
    return {'r_catepost':r_catepost,'r_recpost':r_recpost,'r_filepost':r_filepost}