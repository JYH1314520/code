
from django import template
from main.models import newsList


register = template.Library()
@register.filter(name='getnewsList')
def getnewsList(value):
          return newsList.objects.filter(newsId = value)