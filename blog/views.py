from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'featured_image', 'published_date']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'slug', 'content', 'featured_image', 'published_date']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
