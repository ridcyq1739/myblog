# -*- coding:utf-8 -*-
__author__ = 'kreg'
__date__ = '2018/7/24 13:27'

from django.conf.urls import url

from .views import ArticleDetailView,ArchivesView,CategoryView,TagView,FullWidthView,ContactView,AboutView

app_name = "blog"
urlpatterns = [
    url(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'^about/$',AboutView.as_view(),name='about'),
    url(r'^fullwidth/$',FullWidthView.as_view(),name='fullwidth'),
    url(r'^contact/$',ContactView.as_view(),name='contact'),
    ]