from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import PostUz
from posts.models import Theme, Category

def home(request):
    return render(request, 'index.html')


def post_list(request):
    return render(request, 'post_list.html')


def post_detail(request, **kwargs):
    id = kwargs['pk']

    try: 
        post = get_object_or_404(PostUz, id=id)
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