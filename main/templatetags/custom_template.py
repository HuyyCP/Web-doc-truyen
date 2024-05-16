from django import template

register = template.Library()

@register.filter(name='zip')
def _zip(a, b):
    return zip(a, b)