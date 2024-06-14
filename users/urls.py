from django.urls import path
from . import views

# in a way to avoid conflicts with other apps
# now authomaticall the url will be playground/...
# to call them in the html we will use {% url 'playground:posts_list' %}
app_name = 'users'

# URL Configuration
urlpatterns = [
    path('registration', views.regist_new_user, name="users_registration"),
]