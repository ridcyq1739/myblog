import markdown
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Article,Category
from comments.forms import CommentForm

# Create your views here.

class IndexView(View):
    """
    主页
    """
    def get(self,request):
        article_list = Article.objects.all()

        context = {
            'article_list': article_list,
        }
        return render(request,'index.html', context)


class ArticleDetailView(View):
    """
    文章详情
    """
    def get(self,request,article_id):
        article = Article.objects.get(id=int(article_id))
        article.content = markdown.markdown(article.content,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        commentform = CommentForm()
        comment_list = article.comment_set.all()

        context = {
            'article':article,
            'form':commentform,
            'comment_list':comment_list,
        }
        return render(request,'detail.html',context)


class ArchivesView(View):
    """
    归档
    """
    def get(self,request,year,month):
        article_list = Article.objects.filter(created_time__year=year,
                                                 created_time__month=month
                                                 ).order_by('-created_time')

        context = {
            'article_list': article_list,
        }
        return render(request,'index.html',context)


class CategoryView(View):
    """
    分类
    """
    def get(self,request,category_id):
        cate = Category.objects.get(id=int(category_id))
        article_list = Article.objects.filter(category=cate)

        context = {'cate':cate}
        return render(request,'index.html',context)