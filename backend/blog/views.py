from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Like
from django.contrib import messages
from django.http import JsonResponse





def home(request):
    posts = Post.objects.all()
    form = None 
    comment_form = None
    post_comments = {}

    if request.method == 'POST' and request.user.is_authenticated:
        if 'create_post' in request.POST:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, 'Post created successfully.')
                return redirect('home')

        elif 'comment_post_id' in request.POST:
            post_id = request.POST.get('comment_post_id')
            post = get_object_or_404(Post, id=post_id)
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.success(request, "Your comment has been added!")
                return redirect('home')

    if request.user.is_authenticated:
        form = PostForm()
        comment_form = CommentForm()

    for post in posts:
        post_comments[post.id] = post.comments.all()

    context = {
        'posts': posts,
        'form': form,
        'comment_form': comment_form,
        'post_comments': post_comments,
    }
    return render(request, "blog/home.html", context)


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('home')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/home.html', {'form': form, 'posts': Post.objects.all()})


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def getLogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Thay 'home' bằng URL bạn muốn chuyển hướng tới
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'blog/login.html')


def getSignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'blog/register.html')

        User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, 'User created successfully. You can now log in.')
        return redirect('login')  # Thay 'login' bằng URL của trang đăng nhập

    return render(request, 'blog/register.html')




@login_required(login_url='signin')
def like_post(request):
    username = request.user
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = Like.objects.filter(post=post, author=request.user).first()

    if like_filter is None:
        new_like = Like.objects.create(post=post, author=request.user)
        post.no_of_likes += 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes -= 1
        post.save()
        return redirect('/')
