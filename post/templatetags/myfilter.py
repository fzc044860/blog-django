#coding=utf-8
'''
按markdown方式处理文本
'''
from django.template import Library

register = Library()

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)

