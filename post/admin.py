from django.contrib import admin
from .models import *

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):  #后台显示更多字段
    list_display = ('title','created')

admin.site.register(Category)  #注册数据表到admin后台
admin.site.register(Tag)
admin.site.register(Post,PostModelAdmin) #后台显示更多字段

