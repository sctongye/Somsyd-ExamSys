# -*- coding: utf-8 -*-
"""
Created by @南卡统爷 on 3/31/20 1:31 PM.
"""
__author__ = '@SCTongYe'


from django import template

register = template.Library()


@register.filter(name='score_format')
def score_format(value, arg):
    return str(value) + ' / ' + str(arg)


@register.filter(name='get_user_answer')
def get_user_answer(value, arg):
    return value[str(arg)]