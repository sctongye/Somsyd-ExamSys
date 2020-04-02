# -*- coding: utf-8 -*-
"""
Created by @南卡统爷 on 3/27/20 11:26 PM.
"""
__author__ = '@SCTongYe'

from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登录登出
    path('login/', views.User_login.as_view(), name='login'),
    path('logout/', views.User_logout.as_view(), name='logout'),

    # # 用户注册
    # path('register/', views.User_register.as_view(), name='register'),

    # 用户删除
    path('delete/<int:id>/', views.User_delete.as_view(), name='delete'),

    # 用户信息
    path('edit/<int:id>/', views.Profile_edit.as_view(), name='edit'),


]