from django import template
from django.shortcuts import get_list_or_404
from quotes.models import Quote
from posts.models import Theme, Category, About, Post
from postsuz.models import CategoryUz, AboutUz, ThemeUz
from pages.models import Page

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
    'categories' : categories,
    'url': 'uz' if 'uz' in url else 'ru' 
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
  url = kwargs['url']

  if 'uz' in url:  
    try:
      about = AboutUz.objects.all()[0]
    except AboutUz.DoesNotExist:
      about = None

    return {
      'intro_text' : about.blog_intro
    }

  try:
    about = About.objects.all()[0]
  except About.DoesNotExist:
    about = None

  return {
    'intro_text' : about.blog_intro
  }


@register.inclusion_tag('includes/recent_posts.html', takes_context=True)
def recent_posts_data(context, *args, **kwargs):  
  try:
    main_post = get_list_or_404(Post, main=True)[0]
    posts = get_list_or_404(Post, main=False)
  except Post.DoesNotExist:
    posts = None

  return {
    'recent_posts' : posts,
    'main_post': main_post
  }

@register.inclusion_tag('includes/stats.html', takes_context=True)
def stats_data(context, *args, **kwargs):  
  url = kwargs['url']
  
  info_heading_ru = "В мире каждый год более 35 миллионов людей умирают от неинфекционных болезней."
  info_heading_uz = "Dunyoda har yili 35 milliondan ortiq odam yuqumli bo'lmagan kasalliklardan vafot etadi."
  
  info_text_ru = "Большинство смертей можно было бы предотвратить, поменяв образ жизни людей. Исследования показали, что курение, употребление алкоголя в больших количествах, неправильное питание и сидячий образ жизни являются основным рисками развития НИЗ."
  info_text_uz = "Aksariyat o'limlarni odamlarning yashash tarzini o'zgartirish orqali oldini olish mumkin. Tadqiqotlar shuni ko'rsatdiki, chekish, ko'p spirtli ichimliklar, noto'g'ri ovqatlanish va harakatsiz turmush tarzi NCD rivojlanishining asosiy xavfi hisoblanadi."
  
  stats_uz = {
    'first': {
      'number': 18.6,
      'text': "mln. o'lim xolatlari yurak-qon tomir kasalliklari tufayli"
    },

    'second': {
      'number': 6.7,
      'text': "mln. o'lim xolatlari shakar diabeti tufayli"
    },

    'third': {
      'number': 10,
      'text': "mln. o'lim xolatlari saratonning turli xillari tufayli"
    },
  }

  stats_ru = {
    'first': {
      'number': 18.6,
      'text': 'миллионов смертей от ССЗ'
    },

    'second': {
      'number': 6.7,
      'text': 'миллионов от сахарного диабета'
    },

    'third': {
      'number': 10,
      'text': 'миллионов от различных видов рака'
    },
  }

  return {
    'heading': info_heading_uz if 'uz' in url else info_heading_ru,
    'text': info_text_uz if 'uz' in url else info_text_ru,
    'stats': stats_uz if 'uz' in url else stats_ru  
  }



@register.inclusion_tag('includes/related_posts.html', takes_context=True)
def related_posts(context, *args, **kwargs):  
  
  category = kwargs['category']

  try:
    posts = get_list_or_404(Post, category=category)
  except Post.DoesNotExist:
    posts = None

  return {
    'posts': posts
  }


@register.inclusion_tag('includes/starter.html', takes_context=True)
def starter(context, *args, **kwargs):
  url = kwargs['url']

  if 'uz' in url:  
    try:
      pages = Page.objects.all()
    except Page.DoesNotExist:
      pages = None

    return {
      'page' : pages
    }