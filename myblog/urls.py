"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url,include
from myblog.settings import MEDIA_ROOT,STATIC_ROOT
from django.views.static import serve
from blog.views import IndexView
from django.conf.urls import handler404,handler500


import xadmin


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^blog/', include('blog.urls' ,namespace="blog")),
    url(r'^comment/', include('comments.urls' ,namespace="comments")),

    #富文本
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    #s上传文件目录
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

]

#全局404页面配置
handler404 = 'blog.views.page_not_found'

#全局500页面配置
handler500 = 'blog.views.page_error'