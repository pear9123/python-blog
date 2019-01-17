from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as django_logout
from .forms import UserForm, LoginForm
from django.http import HttpResponse
from django.template import RequestContext


# Create your views here.
class PostLV(ListView):
    model = Post
    # 어떤 데이터를 꺼내쓸래??
    context_object_name = 'post_list'

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html',{'post':post})


#member 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'member/adduser.html', {'form': form})

# member 로그인
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 아이디와 패스워드를 확인해 주세요')
    else:
        form = LoginForm()
        return render(request, 'member/login.html', {'form':form})

# member 로그아웃
def logout(request):
    django_logout(request)
    return redirect('index')
