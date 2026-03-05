from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import Post
from .forms import PostForm


def get_post_or_404(post_id):
    try:
        return Post.objects.get(id=post_id)
    except Exception:
        raise Http404('Post not found')


def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_post_or_404(post_id)
    return render(request, 'post_detail.html', {'object': post})


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


def post_delete(request, post_id):
    post = get_post_or_404(post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'object': post})
