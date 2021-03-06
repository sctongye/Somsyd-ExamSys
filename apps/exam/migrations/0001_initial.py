# Generated by Django 3.0.4 on 2020-03-31 21:54

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '科目',
                'verbose_name_plural': '科目',
            },
        ),
        migrations.CreateModel(
            name='TestParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sys_interface_title', models.CharField(max_length=200, verbose_name='系统显示名称')),
                ('test_time', models.CharField(max_length=3, verbose_name='考试时长(min)')),
            ],
            options={
                'verbose_name': '考试系统参数设置',
                'verbose_name_plural': '考试系统参数设置',
            },
        ),
        migrations.CreateModel(
            name='UserTestRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='得分')),
                ('total_score', models.IntegerField(default=0, verbose_name='测验总分')),
                ('tested_questions', models.CharField(max_length=200, verbose_name='所测试题目pk值')),
                ('incorrect_question', models.CharField(blank=True, max_length=200, null=True, verbose_name='做错题目pk值')),
                ('user_answer', models.TextField(blank=True, null=True, verbose_name='所选答案')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '考试记录',
                'verbose_name_plural': '考试记录',
            },
        ),
        migrations.CreateModel(
            name='QuestionPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('ss', '单选'), ('ms', '多选'), ('tf', '判断题'), ('hand_fill_num', '直接填答案'), ('hand_fill_answer', '大段作答-问答')], default='ss', max_length=20, verbose_name='题目类型')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='题目内容')),
                ('opt_a', models.CharField(default='A. ', max_length=200, verbose_name='选项A')),
                ('opt_b', models.CharField(default='B. ', max_length=200, verbose_name='选项B')),
                ('opt_c', models.CharField(default='C. ', max_length=200, verbose_name='选项C')),
                ('opt_d', models.CharField(default='D. ', max_length=200, verbose_name='选项D')),
                ('answer', models.CharField(max_length=20, verbose_name='正确答案')),
                ('score', models.IntegerField(default=10, verbose_name='分值')),
                ('note', models.TextField(default='备注信息', verbose_name='备注信息')),
                ('blank_field', models.TextField(blank=True, null=True, verbose_name='问答题答案')),
                ('boolt', models.TextField(default='True', verbose_name='判断正误正确选项')),
                ('boolf', models.TextField(default='False', verbose_name='判断正误错误选项')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否启用')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='exam.Course')),
            ],
            options={
                'verbose_name': '题库',
                'verbose_name_plural': '题库',
                'ordering': ('-created',),
            },
        ),
    ]
