from django import template
from quotes.models import Quote

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