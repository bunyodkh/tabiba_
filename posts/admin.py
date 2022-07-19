from django.contrib import admin

from .models import Post, Theme, Category, About


admin.site.register(Post)
admin.site.register(Theme)
admin.site.register(Category)
admin.site.register(About)