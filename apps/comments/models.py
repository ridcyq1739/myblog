from django.db import models
from django.utils.six import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Comment(models.Model):
    """
    评论
    """
    name = models.CharField(max_length=100,verbose_name= "姓名")
    email = models.EmailField(max_length=255,verbose_name= "邮箱")
    url = models.URLField(blank=True,verbose_name= "网址")
    text = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    article = models.ForeignKey('blog.Article',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]

