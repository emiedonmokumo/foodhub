from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def get_post_or_404(post_id):
    try:
        return Post.objects.get(id=post_id)
    except Exception:
        raise Http404('Post not found')


def landing_page(request):
    posts = Post.objects.order_by('-published_date')[:6]
    return render(request, 'landing.html', {'posts': posts})


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            error = "Invalid username or password"
            
    return render(request, 'admin_login.html', {'error': error})


def admin_logout(request):
    logout(request)
    return redirect('landing_page')


def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_post_or_404(post_id)
    return render(request, 'post_detail.html', {'object': post})


@login_required(login_url='admin_login')
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post(**data)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


@login_required(login_url='admin_login')
def post_edit(request, post_id):
    post = get_post_or_404(post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            for k, v in form.cleaned_data.items():
                setattr(post, k, v)
            post.updated_at = post.updated_at
            post.save()
            return redirect('post_list')
    else:
        initial = {
            'title': post.title,
            'slug': post.slug,
            'content': post.content,
            'featured_image': post.featured_image,
            'published_date': post.published_date,
        }
        form = PostForm(initial=initial)
    return render(request, 'post_form.html', {'form': form, 'object': post})


@login_required(login_url='admin_login')
def post_delete(request, post_id):
    post = get_post_or_404(post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'object': post})
