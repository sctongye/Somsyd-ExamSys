from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth.models import User


class TestParams(models.Model):
    sys_interface_title = models.CharField(max_length=200, verbose_name="系统显示名称")
    test_time = models.CharField(max_length=3, verbose_name="考试时长(min)")

    class Meta:
        verbose_name = "考试系统参数设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.test_time


class Course(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "科目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class QuestionPool(models.Model):
    course = models.ForeignKey(
        Course,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='course'
    )
    question_type = models.CharField(max_length=20, choices=(("ss", "单选"), ("ms", "多选"), ("tf", "判断题"), ("hand_fill_num", "直接填答案"), ("hand_fill_answer", "大段作答-问答")), default="ss", verbose_name="题目类型")
    weighting = models.IntegerField(verbose_name='排列权重', null=True, blank=True)
    content = RichTextUploadingField(verbose_name='题目内容')
    opt_a = models.CharField(max_length=200, verbose_name="选项A", default="A. ")
    opt_b = models.CharField(max_length=200, verbose_name="选项B", default="B. ")
    opt_c = models.CharField(max_length=200, verbose_name="选项C", default="C. ")
    opt_d = models.CharField(max_length=200, verbose_name="选项D", default="D. ")
    answer = models.CharField(max_length=20, verbose_name="正确答案")
    score = models.IntegerField(verbose_name="分值", default=10)
    note = models.TextField(verbose_name="备注信息", default="备注信息\n")
    blank_field = models.TextField(verbose_name="问答题答案", null=True, blank=True)
    boolt = models.TextField(verbose_name="判断正误正确选项", default="True")
    boolf = models.TextField(verbose_name="判断正误错误选项", default="False")
    is_active = models.BooleanField(default=True, verbose_name="是否启用")

    # cover_img = models.ImageField(upload_to='/%Y%m%d/', blank=True)

    created = models.DateTimeField(default=timezone.now)

    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列，最新的文章总是在网页的最上方
        ordering = ('-created',)
        verbose_name = "题库"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return "{0}/ {1} - {2}".format(self.is_active, self.created.strftime('%Y-%m-%d (%H点)'), self.note[:16])
        return self.note[:10]

    def save(self, *args, **kwargs):

        if self.question_type == "ss":
            self.weighting = 1
        if self.question_type == "ms":
            self.weighting = 2
        if self.question_type == "tf":
            self.weighting = 3
        if self.question_type == "hand_fill_num":
            self.weighting = 4
        if self.question_type == "hand_fill_answer":
            self.weighting = 5

        super().save(*args, **kwargs)




# 每经过一次测试以后总情况（考试科目，得分，实体总分数。考试时间）
class UserTestRecord(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="用户"
    )

    # course = models.ForeignKey(
    #     Course,
    #     on_delete=models.CASCADE,
    #     verbose_name="科目"
    # )

    score = models.IntegerField(verbose_name="得分", default=0)
    total_score = models.IntegerField(verbose_name="测验总分", default=0)
    tested_questions = models.CharField(max_length=200, verbose_name="所测试题目pk值")
    incorrect_question = models.CharField(max_length=200, null=True, blank=True, verbose_name="做错题目pk值")
    user_answer = models.TextField(verbose_name="所选答案", null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = "考试记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0} - {1}".format(self.user, self.created)


class UsefulLinkBookmark(models.Model):
    title = models.CharField(max_length=100, verbose_name='名称')
    url = models.CharField(max_length=300, verbose_name='链接')
    note = models.TextField(verbose_name="备注信息", default="备注信息")

    class Meta:
        verbose_name = "Bookmark"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title