from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from datetime import datetime
from django.utils.six import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    '''
    分类
    '''
    name = models.CharField(max_length= 50,verbose_name= "类名")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length= 50,verbose_name= "标签名")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length= 50,verbose_name= "标题")
    content = UEditorField(verbose_name=u'文章内容', width=600, height=300, imagePath="blog/ueditor/",
                filePath="blog/ueditor/", default="")
    created_time = models.DateTimeField(default=datetime.now,verbose_name= "创建时间")
    modified_time = models.DateTimeField(default=datetime.now,verbose_name= "最后一次修改")
    excerpt = models.CharField(max_length= 200,blank=True,verbose_name= "摘要")
    category = models.ForeignKey(Category,verbose_name= "类型",on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True,verbose_name= "标签")
    author = models.ForeignKey(User,verbose_name= "作者",on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_comment_num(self):
        return self.comment_set.all().count()