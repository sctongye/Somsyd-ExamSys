from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
# 引入验证登录的装饰器
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile


# 用户登录
class User_login(View):

    def get(self, request):
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)

    def post(self, request):
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("index")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")


# 用户退出
class User_logout(View):

    def get(self, request):
        logout(request)
        return redirect("index")


# 用户注册
class User_register(View):

    def get(self, request):
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)

    def post(self, request):
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("index")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")


# 删除用户
@method_decorator(login_required, name="dispatch")
class User_delete(View):
    def post(self, request, id):
        user = User.objects.get(id=id)
        # 验证登录用户、待删除用户是否相同
        if request.user == user:
            #退出登录，删除数据并返回博客列表
            logout(request)
            user.delete()
            return redirect("index")
        else:
            return HttpResponse("你没有删除操作的权限。")

    # def get(self, request):
    #     return HttpResponse("仅接受post请求。")


# 编辑用户信息
@method_decorator(login_required, name="dispatch")
class Profile_edit(View):

    def post(self, request, id):
        user = User.objects.get(id=id)
        # user_id 是 OneToOneField 自动生成的字段
        if Profile.objects.filter(user_id=id).exists():
            profile = Profile.objects.get(user_id=id)
        else:
            profile = Profile.objects.create(user=user)

        # 验证修改数据者，是否为用户本人
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息。")

        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            # 取得清洗后的合法数据

            profile_cd = profile_form.cleaned_data

            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]

            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            profile.save()
            # 带参数的 redirect()
            # return redirect("userprofile:edit", id=id)
            return redirect("index")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")

    def get(self, request, id):

        user = User.objects.get(id=id)
        # user_id 是 OneToOneField 自动生成的字段
        # profile = Profile.objects.get(user_id=id)

        if Profile.objects.filter(user_id=id).exists():
            profile = Profile.objects.get(user_id=id)
        else:
            profile = Profile.objects.create(user=user)

        profile_form = ProfileForm()
        context = { 'profile_form': profile_form, 'profile': profile, 'user': user }
        return render(request, 'userprofile/edit.html', context)