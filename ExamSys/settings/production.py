# -*- coding: utf-8 -*-
"""
Created by @南卡统爷 on 3/29/20 4:39 PM.
"""
__author__ = '@SCTongYe'


from .base import *
from ExamSys.settings import SensitiveInfo

ALLOWED_HOSTS = SensitiveInfo.PROD_ALLOWED_HOSTS

DEBUG = False
print("RPi4服务器远程开发环境")

DATABASES = SensitiveInfo.PROD_DATABASES

# STATICFILES_DIRS = ()
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, "static")


