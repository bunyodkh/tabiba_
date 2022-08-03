import re
from unicodedata import category
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.postgres.search import SearchVector

from .models import Post, Theme, Category
from postsuz.models import PostUz

def home(request):
    return render(request, 'index.html')


def search_for(request):
    if request.method == 'GET':      
        q =  request.GET.get('q')
        try:
            posts_title = Post.objects.filter(title__icontains=q)
            posts_body = Post.objects.filter(full_content__icontains=q)
        except:
            posts_title = None
            posts_body = None
    
    print(posts_title)
    print(posts_body)
    return render(request, 'search.html', { 'postsbytitle': posts_title, 'postsbybody': posts_body, 'q': q })


def post_detail(request, **kwargs):
    id = kwargs['pk']

    try: 
        post = get_object_or_404(Post, id=id)
    except:
        post = None

    return render(request, 'post_detail.html', { 'post': post })



def theme_detail(request, **kwargs):
    id = kwargs['pk']
    theme = Theme.objects.get(id=id)
    try: 
        posts = theme.post_set.all()
    except:
        posts = None
    return render(request, 'theme_detail.html', { 'posts': posts, 'theme': theme })



def category_detail(request, **kwargs):
    id = kwargs['pk']
    category =  get_object_or_404(Category, id=id)
    try: 
        posts = category.post_set.all()
    except:
        posts = None
    return render(request, 'theme_detail.html', { 'posts': posts, 'category': category })


# serves 404.html page
def e_handler404(request, exception=None):
    return render(request, '404.html', {}, status=404)

# serves 500.html page
def e_handler500(request, exception=None):
    return render(request, '500.html', {}, status=500)