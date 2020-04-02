# -*- coding: utf-8 -*-
"""
Created by @南卡统爷 on 3/30/20 12:22 AM.
"""
__author__ = '@SCTongYe'


# 引入表单类
from django import forms
# 引入文章模型
from .models import QuestionPool

# 写文章的表单类
class QuestionPoolForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = QuestionPool
        # 定义表单包含的字段
        fields = ('content', 'opt_a', 'opt_b', 'opt_c', 'opt_d', 'boolt', 'boolf')
