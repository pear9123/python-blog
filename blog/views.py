from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
class PostLV(ListView):
    model = Post
    # 어떤 데이터를 꺼내쓸래??
    context_object_name = 'post_list'

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html',{'post':post})


#member
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'blog/adduser.html', {'form': form})
