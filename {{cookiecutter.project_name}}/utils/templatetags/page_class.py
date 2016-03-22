from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def page_class(context):
    request = context['request']
    if hasattr(request.resolver_match, 'url_name'):
        return 'page-%s' % request.resolver_match.url_name
    return ''
