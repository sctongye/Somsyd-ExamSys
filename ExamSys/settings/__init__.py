# -*- coding: utf-8 -*-
"""
Created by @南卡统爷 on 3/29/20 4:39 PM.
"""
__author__ = '@SCTongYe'


import os

if os.environ.get('MYSITE_CONFIG') == "pc":
    print("本地 Windows PC 上运行中")
    from .local import *
elif os.environ.get('MYSITE_CONFIG') == "ubuntu_p73":
    print("本地 Linux Ubuntu P73 上运行中")
    from .local import *
else:
    from .production import *


