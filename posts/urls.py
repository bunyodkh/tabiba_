from django.urls import path
from .views import home, post_list, post_detail, theme_detail, category_detail

app_name = 'posts'

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='post-list'),
    path('posts/<str:pk>', post_detail, name='post-detail'),
    path('posts/theme/<str:pk>', theme_detail, name='theme-detail'),
    path('posts/caregory/<str:pk>', category_detail, name='category-detail'),
]