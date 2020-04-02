from django.contrib import admin
from .models import QuestionPool, Course, UserTestRecord, TestParams, UsefulLinkBookmark




admin.site.register(Course)
admin.site.register(UserTestRecord)
admin.site.register(TestParams)
admin.site.register(UsefulLinkBookmark)

@admin.register(QuestionPool)
class QuestionPoolAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'course', 'is_active', 'question_type', 'score', 'created')
    ordering = ('-is_active','-created')
    list_editable = ['is_active', 'course', 'score']
    list_filter = ('question_type', 'course')
    list_per_page = 100
    actions = ['make_is_not_active']

    # 点击保存并继续编辑
    save_as_continue = True

    # save按钮的位置,是True则显示在页面上方
    save_on_top = True

    def make_is_not_active(self, request, queryset):
        queryset.update(is_active=False)

    make_is_not_active.short_description = "Mark selected as not active"


# class MyAdminSite(admin.AdminSite):
#     site_header = '我的管理网站'
# admin_site = MyAdminSite()
