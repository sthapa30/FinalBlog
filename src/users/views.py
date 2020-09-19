from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
            
    context = {
        'form' : form
    }
    return render(request,'register.html',context)
@login_required
def profile(request):
    post_list = Post.objects.filter(author__user=request.user)
    img_url = post_list[0].author.profile_picture.url
    context = {
        'post_list': post_list,
        'img_url': img_url
    }
    return render(request,'profile.html',context)
    
