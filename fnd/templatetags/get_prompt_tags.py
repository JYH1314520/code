from django import template
from django.core.cache import cache
from fnd.models import fnd_prompts
from webapp.basefun import convert_to_dicts


register = template.Library()

#@register.tag(name='getprompt')
@register.simple_tag()
def getprompt(prompt_code):
    promptslist = cache.get('fnd_prompts'+ prompt_code)
    if not promptslist:
        return prompt_code
    return promptslist