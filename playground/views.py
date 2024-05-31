from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view: function that takes a web request and returns a web response
def say_hello(request):
    return HttpResponse("Hello, Django!")