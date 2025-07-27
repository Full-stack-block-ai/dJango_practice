# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
news = {
    'blog_page': 'Blog page',
    'media_page': 'Media page'
}
#takes in a request to check out the view and returns a http response
#from from django.http import HttpResponse 
def index(request):
    return HttpResponse("hello this is my first view inside my_app")


# dynamic routing example 
def newsfeed(request, topic):
    return HttpResponse( news[topic])