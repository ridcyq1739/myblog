# -*- coding:utf-8 -*-
__author__ = 'kreg'
__date__ = '2018/7/24 19:27'

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

