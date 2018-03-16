from django import template 
from django.urls.base import resolve 

register = template.Library()

@register.simple_tag
def get_page_title():
    title = 'Willian Tessaro Lunardi'
    return title

def get_name_url():
    current_url = resolve(request.path_info).url_name;
    return current_url