# -*- coding:utf-8 -*-
__author__ = 'kreg'
__date__ = '2018/7/24 17:02'

from ..models import Article,Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:5]

@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()
