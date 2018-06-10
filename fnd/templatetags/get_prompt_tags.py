from django import template
from django.core.cache import cache
from fnd.models import fnd_prompts
from webapp.basefun import convert_to_dicts


register = template.Library()



#@register.tag(name='getprompt')
@register.simple_tag()
def getprompt(prompt_code):
    promptslist = cache.get('fnd_prompts')
    if not promptslist:
        a_list = fnd_prompts.objects.filter(lang="zh-cn")
        print('初始化将查询到的数据加载到缓存中')
        row = convert_to_dicts(a_list)
        cache.set('fnd_prompts', row)
    promptslist = cache.get('fnd_prompts')
    for _prompt in promptslist:
        if prompt_code == _prompt.get("prompt_code"):
            return _prompt.get("description")
        else:
            return "not_find_prompt"
    return "not_find_prompt"