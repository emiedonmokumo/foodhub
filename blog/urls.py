from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/add/', views.post_add, name='post_add'),
    path('post/<str:post_id>/', views.post_detail, name='post_detail'),
    path('post/<str:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<str:post_id>/delete/', views.post_delete, name='post_delete'),
]
