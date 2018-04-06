from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('publications/', views.publications, name='publications'),
	path('research/', views.research, name='research'),	
	path('code/', views.code, name='code'),
	path('contact/', views.contact, name='contact'),
	path('registration/', views.registration, name='registration'), 
]
