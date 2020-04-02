from django.contrib import admin
# from exam.admin import admin_site
from django.urls import path, include, re_path
from django.views.static import serve
from ExamSys.settings import MEDIA_ROOT
try:
    from ExamSys.settings import STATIC_ROOT
except:
    from ExamSys.settings import STATICFILES_DIRS
    STATIC_ROOT = STATICFILES_DIRS[0]
# from django.conf import settings
# from django.conf.urls.static import static
from exam.views import *


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('exam_page/', ExamPage.as_view(), name='exam_page'),
    path('final_page/', ExamPage.as_view(), name='final_page'),

    path('admin/', admin.site.urls),
    # path('admin/', admin_site.urls),

    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # path('password-reset/', include('password_reset.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')), #添加ckeditor的url到项目中

    # Static 文件
    re_path(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)/$', serve, {"document_root": STATIC_ROOT}),
]
