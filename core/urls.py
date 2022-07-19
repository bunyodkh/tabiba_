from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import e_handler404
from posts.views import e_handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('uz/', include('postsuz.urls')),
    path('pages/', include('pages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler404 = e_handler404
handler500 = e_handler500

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)