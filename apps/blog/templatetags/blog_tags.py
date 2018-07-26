# -*- coding:utf-8 -*-
__author__ = 'kreg'
__date__ = '2018/7/24 17:02'
from django.db.models.aggregates import Count
from ..models import Article,Category,Tag
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
    return Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
