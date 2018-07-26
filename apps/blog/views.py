from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Article,Category,Tag,Contact
from .forms import ContactForm
from comments.forms import CommentForm
# Create your views here.

class IndexView(View):
    """
    主页
    """
    def get(self,request):
        articles = Article.objects.all()
        q = request.GET.get('q','')
        if q:
            articles = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

        tags = Tag.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 3, request=request)

        articles = p.page(page)

        context = {
            'articles': articles,
            'tags': tags,
        }
        return render(request,'index.html', context)


class ArticleDetailView(View):
    """
    文章详情
    """
    def get(self,request,article_id):
        article = Article.objects.get(id=int(article_id))
        article.views += 1
        article.save()
        articles = Article.objects.all()
        q = request.GET.get('q', '')
        if q:
            articles = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

        categorys = Category.objects.all()
        commentform = CommentForm()
        comment_list = article.comment_set.all()

        context = {
            'articles':articles,
            'article':article,
            'form':commentform,
            'comment_list':comment_list,
            'categorys':categorys,
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
        articles = Article.objects.filter(category=cate)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 3, request=request)

        articles = p.page(page)
        context = {
                'articles':articles,
                'cate':cate,
                   }
        return render(request,'index.html',context)


class TagView(View):
    """
    标签
    """
    def get(self,request,tag_id):
        tag = Tag.objects.get(id=int(tag_id))
        articles = Article.objects.filter(tags=tag)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 3, request=request)

        articles = p.page(page)
        context = {
                'tag':tag,
                'articles': articles,
                   }
        return render(request,'index.html',context)



class AboutView(View):
    """
    关于我
    """
    def get(self,request):
        return render(request,'about.html',{})


class FullWidthView(View):
    """
    博客页面
    """
    def get(self,request):
        articles = Article.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 3, request=request)

        articles = p.page(page)

        context = {
            'articles':articles,
        }
        return render(request,'full-width.html',context)


class ContactView(View):
    """
    联系
    """
    def get(self,request):
        return render(request,'contact.html',{})

    def post(self,request):
        forms = ContactForm(request.POST)
        if forms.is_valid():
            contact = forms.save(commit=False)
            contact.save()
            return render(request,'contact.html',{})
        return render(request, 'contact.html', {})


def page_not_found(request,exception):
    #全局404处理函数
    return render(request,'404.html')

def page_error(request,exception):
    #全局500处理函数
    return render(request,'500.html')
