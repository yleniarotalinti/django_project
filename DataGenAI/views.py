from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# view: function that takes a web request and returns a web response
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Ylenia'})
