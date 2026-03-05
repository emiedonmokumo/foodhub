from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('admin-dashboard/', views.post_list, name='post_list'),
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('post/add/', views.post_add, name='post_add'),
    path('post/<str:post_id>/', views.post_detail, name='post_detail'),
    path('admin-dashboard/post/<str:post_id>/', views.admin_post_detail, name='admin_post_detail'),
    path('post/<str:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<str:post_id>/delete/', views.post_delete, name='post_delete'),
]
