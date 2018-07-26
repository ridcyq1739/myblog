# -*- coding:utf-8 -*-
__author__ = 'kreg'
__date__ = '2018/7/26 11:50'

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']