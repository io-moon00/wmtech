from django import template

register = template.Library()

@register.simple_tag
def active_class(page, current_page):
    return 'border-main text-gray-900' if page == current_page else 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'

@register.filter
def get_tooltip_name(name):
    return f'{name.replace(" ", "_").lower()}'