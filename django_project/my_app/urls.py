from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('publications/', views.publications, name='publications'),
	path('research/', views.research, name='research'),	
	path('comment/', views.comment, name='comment'),
	path('code/', views.code, name='code'), 
]
