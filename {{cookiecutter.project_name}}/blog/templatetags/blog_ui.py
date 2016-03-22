from django import template
register = template.Library()


@register.inclusion_tag('blog/partials/category_badge.html')
def category_badge(category):
    return {'category': category}

@register.inclusion_tag('blog/partials/post_thumbnail.html')
def render_post(post):
    return {'post': post}
