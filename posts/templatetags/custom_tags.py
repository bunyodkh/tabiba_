from django import template
from django.shortcuts import get_list_or_404
from quotes.models import Quote
from posts.models import Theme, Category, About, Post
from postsuz.models import CategoryUz, AboutUz, ThemeUz

register = template.Library()

@register.inclusion_tag('includes/quotes.html', takes_context=True)
def quote_data(context, *args, **kwargs):  
  try:
    quote = Quote.objects.get(active=True)
    print(quote)
  except Quote.DoesNotExist:
    quote = None

  return {
    'quote' : quote
  }


@register.inclusion_tag('includes/themes.html', takes_context=True)
def themes_data(context, *args, **kwargs):  
  url = kwargs['url']

  if 'uz' in url:
    try:
      themes = ThemeUz.objects.all()
    except ThemeUz.DoesNotExist:
      themes = None
    return {
      'themes' : themes,
      'lang': 'uz'
    }
  
  try:
    themes = Theme.objects.all()
  except Theme.DoesNotExist:
    themes = None
  return {
    'themes' : themes,
    'lang': 'ru'
  }


@register.inclusion_tag('includes/nav.html', takes_context=True)
def nav_data(context, *args, **kwargs):  

  url = kwargs['url']

  if 'uz' in url:
    try:
      categories = CategoryUz.objects.all()
    except CategoryUz.DoesNotExist:
      categories = None

    return {
      'categories' : categories
    }
  
  try:
    categories = Category.objects.all()
  except Theme.DoesNotExist:
    categories = None

  return {
    'categories' : categories
  }



@register.inclusion_tag('includes/about.html', takes_context=True)
def about_data(context, *args, **kwargs):  
  
  url = kwargs['url']

  if url and 'uz' in url:
    try:
      about_text = AboutUz.objects.all()[0]
    except AboutUz.DoesNotExist:
      about_text = None

    return {
      'about' : about_text,
      'lang': 'uz'
    }
  
  try:
    about_text = About.objects.all()[0]
  except About.DoesNotExist:
    about_text = None

  return {
    'about' : about_text,
    'lang': 'ru'
  }



@register.inclusion_tag('includes/intro_text.html', takes_context=True)
def intro_text_data(context, *args, **kwargs):  
  try:
    about = About.objects.all()[0]
  except Theme.DoesNotExist:
    about = None

  return {
    'intro_text' : about.blog_intro
  }



@register.inclusion_tag('includes/recent_posts.html', takes_context=True)
def recent_posts_data(context, *args, **kwargs):  
  try:
    main_post = get_list_or_404(Post, main=True)[0]
    posts = get_list_or_404(Post, main=False)
  except Theme.DoesNotExist:
    posts = None

  return {
    'recent_posts' : posts,
    'main_post': main_post
  }
