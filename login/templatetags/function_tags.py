
from django import template
from login.models import function


register = template.Library()
@register.filter(name='getNextfunction')
def getNextfunction(value):
          return function.objects.filter(parent_function_id = value)