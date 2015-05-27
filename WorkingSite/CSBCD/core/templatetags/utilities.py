from django import template
from django.template.defaulttags import URLNode, url as url_tag

register = template.Library()

@register.tag
def url(parser, token):
    validator = url_tag(parser, token)
    return SmartURLNode(validator.view_name, validator.args, validator.kwargs, validator.asvar)

class SmartURL(unicode):
    pass

class SmartURLNode(URLNode):
    def render(self, context):
        resolved_view_home = self.view_name.resolve(context)
