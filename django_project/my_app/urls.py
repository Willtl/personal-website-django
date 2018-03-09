from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('comment/', views.comment, name='comment_1'), 
]
