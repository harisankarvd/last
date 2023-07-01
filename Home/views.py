from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def hello(request):
    return HttpResponse('<h1>hello welcome</h1>')


def index(request):
    temp= loader.get_template("index1.html")
    # n=input("enter ur name : ")
    student={'name':'ammu'}
    return HttpResponse(temp.render(student))