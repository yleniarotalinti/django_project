from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.http import JsonResponse
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# view: function that takes a web request and returns a web response

def show_my_name(request):
    # Pass a dictionary to the template to render the template with some data (in the html file you can access the data using the key)
    posts = Post.objects.all().order_by('-created_at')    #descending order
    return render(request, 'about.html', {'posts': posts}) 

def show_my_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})

## CRUD METHODS (use of the serialiser)
@api_view(['GET', 'POST'])
def get_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serialised_posts = PostSerializer(posts, many=True)
        return JsonResponse({"posts_list":serialised_posts.data}, safe=False)
    elif request.method == 'POST':
        serialized_new_post = PostSerializer(data=request.data)
        if serialized_new_post.is_valid():
            serialized_new_post.save()
            return Response(serialized_new_post.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def get_post(request,id):
    try:
        post = Post.objects.filter(id=id) #id is a default field in django. We pass it as a parameter in the url
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized_post = PostSerializer(post, many=True)
        return Response(serialized_post.data)
    elif request.method == 'PUT':
        serialized_post = PostSerializer(post, data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data)
        return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    











