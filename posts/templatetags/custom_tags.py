from django import template
from django.shortcuts import get_list_or_404
from quotes.models import Quote
from posts.models import Theme, Category, About, Post

register = template.Library()

@register.inclusion_tag('includes/quotes.html')
def quote_data():  
  try:
    quote = Quote.objects.get(active=True)
    print(quote)
  except Quote.DoesNotExist:
    quote = None

  return {
    'quote' : quote
  }


@register.inclusion_tag('includes/themes.html')
def themes_data():  
  try:
    themes = Theme.objects.all()
  except Theme.DoesNotExist:
    themes = None

  return {
    'themes' : themes
  }


@register.inclusion_tag('includes/nav.html')
def nav_data():  
  try:
    categories = Category.objects.all()
  except Theme.DoesNotExist:
    categories = None

  return {
    'categories' : categories
  }



@register.inclusion_tag('includes/about.html')
def about_data():  
  try:
    about_text = About.objects.all()[0]
  except About.DoesNotExist:
    about_text = None

  return {
    'about' : about_text
  }



@register.inclusion_tag('includes/intro_text.html')
def intro_text_data():  
  try:
    about = About.objects.all()[0]
  except Theme.DoesNotExist:
    about = None

  return {
    'intro_text' : about.blog_intro
  }



@register.inclusion_tag('includes/recent_posts.html')
def recent_posts_data():  
  try:
    main_post = get_list_or_404(Post, main=True)[0]
    posts = get_list_or_404(Post, main=False)
  except Theme.DoesNotExist:
    posts = None

  return {
    'recent_posts' : posts,
    'main_post': main_post
  }
