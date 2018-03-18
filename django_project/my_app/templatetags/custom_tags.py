from django import template 
from django.urls.base import resolve 

register = template.Library()

name = 'Willian Tessaro Lunardi'
email = 'willian.tessarolunardi@uni.lu'


@register.simple_tag
def get_page_title():
    return name 


@register.simple_tag
def get_captcha_key():
    key = '6LeZZU0UAAAAAICQglPp7bgLsM50k9I1RHvvMzWZ'
    return key 


@register.simple_tag
def get_email(): 
    return email 
