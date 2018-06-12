from django import template
from webapp.settings import TRANSLATION_FIELDS

register = template.Library()


class LocalizedContent(template.Node):
    def __init__(self, model, language_code):
        self.model = model
        self.lang = language_code

    def render(self, context):
        model = template.resolve_variable(self.model, context)
        lang = template.resolve_variable(self.lang, context)
        for f in TRANSLATION_FIELDS:
            try:
                setattr(model, f, getattr(model, '%s_%s' % (f, lang)))
            except AttributeError:
                pass
        return ''


@register.tag(name='get_localized_content')
def get_localized_content(parser, token):
    bits = list(token.split_contents())
    if len(bits) != 3:
        raise template.TemplateSyntaxError("'get_localized_content' tag takes exactly 2 arguments")
    return LocalizedContent(model=bits[1], language_code=bits[2])