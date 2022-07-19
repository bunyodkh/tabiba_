from django.shortcuts import render

from .models import Page 

def get_page(request, **kwargs):
    slug = kwargs['slug']
    
    try:
        page = Page.objects.get(slug=slug)
    except:
        page: None
    
    return render(request, 'page_detail.html', { 'page': page })
