from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.
# view: function that takes a web request and returns a web response

def show_my_name(request):
    # Pass a dictionary to the template to render the template with some data (in the html file you can access the data using the key)
    posts = Post.objects.all().order_by('-created_at')    #descending order
    return render(request, 'about.html', {'posts': posts}) 

def show_my_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})




