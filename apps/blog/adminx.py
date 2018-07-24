# -*- coding:utf-8 -*-
__author__ = 'kreg'
__date__ = '2018/7/24 12:43'

import xadmin
from xadmin import views

from .models import Category,Tag,Article


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "myblog"
    menu_style = "accordion"

class CategoryAdmin(object):
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = ['name',]

class TagAdmin(object):
    list_display = ['name', ]
    search_fields = ['name', ]
    list_filter = ['name', ]

class ArticleAdmin(object):
    list_display = ['title','created_time','modified_time','excerpt','category','tags','author', ]
    search_fields = ['title','created_time','modified_time','excerpt','category','tags','author',]
    list_filter = ['title','created_time','modified_time','excerpt','category','tags','author',]
    style_fields = {"content": "ueditor"}


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Article,ArticleAdmin)