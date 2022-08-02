from django.urls import path
from .views import home, post_list, post_detail, theme_detail, category_detail

app_name = 'postsuz'

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='postuz-list'),
    path('posts/<str:pk>', post_detail, name='postuz-detail'),
    path('posts/theme/<str:pk>', theme_detail, name='themeuz-detail'),
    path('posts/caregory/<str:pk>', category_detail, name='categoryuz-detail'),
]