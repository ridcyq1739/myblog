from django.shortcuts import render,redirect
from blog.models import Article
from django.views.generic.base import View
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Comment
from .forms import CommentForm
# Create your views here.


class ArticleCommentView(View):
    """
    评论
    """
    def get(self,request,article_id):
        return redirect(reverse('blog:detail',args=[article_id,]))

    def post(self,request,article_id):
        article = Article.objects.get(id=int(article_id))
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.article = article
            comment.save()

            return redirect(reverse('blog:detail', args=[article_id, ]))

        else:
            comment_list = article.comment_set.all()
            context = {'article': article,
                       'form': commentform,
                       'comment_list': comment_list
                       }
            return render(request, 'detail.html', context=context)





