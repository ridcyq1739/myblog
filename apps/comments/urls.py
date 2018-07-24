# -*- coding:utf-8 -*-
__author__ = 'kreg'
__date__ = '2018/7/24 19:39'

from django.conf.urls import url

from .views import ArticleCommentView

app_name = "comments"
urlpatterns = [
    url(r'^article/(?P<article_id>[0-9]+)/$', ArticleCommentView.as_view(), name='article_comment'),
]