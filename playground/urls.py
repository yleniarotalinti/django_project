from django.urls import path
from . import views

# in a way to avoid conflicts with other apps
# now authomaticall the url will be playground/...
# to call them in the html we will use {% url 'playground:posts_list' %}
app_name = 'playground'

# URL Configuration
urlpatterns = [
    path('', views.show_my_name, name="posts_list"),
    # slug (after :) is a parameter that we pass to the view 
    path('<slug:slug>', views.show_my_post, name="post_detail")
]