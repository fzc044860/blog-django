from django.shortcuts import render,redirect
from post import models
from bolg.utils.pagelist import Pagination

# Create your views here.
def index(request):
    num = request.GET.get('num',1)
    num = int(num)

    #获取所有帖子信息
    queryset = models.Post.objects.all().order_by('-created')

    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset  # 分完页的数据
    page_string = page_object.html()  # 页码
    return render(request,'index.html',locals())

def detail(request,nid):
    '''阅读全文'''
    queryset = models.Post.objects.filter(id=nid).first()
    return render(request,'detail.html',locals())

def post_date(request,year,month):
    queryset = models.Post.objects.filter(created__year=year,created__month=month)
    print(queryset)
    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset  # 分完页的数据
    page_string = page_object.html()  # 页码
    return render(request,'index.html',locals())

from django.views.decorators.cache import cache_page

@cache_page(60*15)
def post_category(request,cid):
    queryset = models.Post.objects.filter(category=cid)
    print(queryset)
    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset  # 分完页的数据
    page_string = page_object.html()  # 页码
    return render(request,'index.html',locals())

