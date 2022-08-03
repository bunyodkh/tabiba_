from django.urls import path
from .views import home, post_detail, theme_detail, category_detail, search_for

app_name = 'posts'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_for, name='search-for'),
    path('posts/<str:pk>', post_detail, name='post-detail'),
    path('posts/theme/<str:pk>', theme_detail, name='theme-detail'),
    path('posts/caregory/<str:pk>', category_detail, name='category-detail'),
]