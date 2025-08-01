from django.urls import path
#imports the views
from . import views

urlpatterns = [
    #connects to app
    #routing so empty string is default , views , string name
    path('', views.index),

    #Page number redirect
    path('<int:num>', views.news_feed_num),
    
    #Dynamic path routing to the news feed view
    path('<topic>', views.news_feed, name='news-feed'),
    

]