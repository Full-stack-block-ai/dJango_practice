from django.urls import path
#imports the views
from . import views

urlpatterns = [
    #connects to app
    #routing so empty string is default , views , string name
    path('', views.index, name='index')
]