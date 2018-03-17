from django import template 
from django.urls.base import resolve 

register = template.Library()

@register.simple_tag
def get_page_title():
    title = 'Willian Tessaro Lunardi'
    return title 