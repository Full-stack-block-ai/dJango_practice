# Create your views here.
from django.http import Http404
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
news = {
    'blog_page': 'Blog page',
    'media_page': 'Media page',
    'about_page': 'About page'
}
#takes in a request to check out the view and returns a http response
#from from django.http import HttpResponse 
def index(request):
    return HttpResponse("hello this is my first view inside my_app")


# dynamic routing example 
def news_feed(request, topic):
    try:
        return HttpResponse( news[topic])
    except:
        return Http404("topic not found")
    

#Diverts page numbers to pages
def news_feed_num(request, num):
    try:
        topic_list = list(news.keys())
        topic = topic_list[num]
        return HttpResponse(topic)
    except:
        return Http404("topic not found")