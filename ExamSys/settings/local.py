# -*- coding: utf-8 -*-
"""
Created by @南卡统爷 on 3/29/20 4:39 PM.
"""
__author__ = '@SCTongYe'


from .base import *
from ExamSys.settings import SensitiveInfo

ALLOWED_HOSTS = SensitiveInfo.LOCAL_ALLOWED_HOSTS

DEBUG = True
print("本地开发环境")

# USE this to link remote server mysql port 3306 to local 3333 port
# ssh -N -L 3333:127.0.0.1:3306 username@xxx.xxx.xxx.xxx -p 22


DATABASES = SensitiveInfo.LOCAL_DATABASES


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
#
# STATIC_ROOT = os.path.join(BASE_DIR, "static")


