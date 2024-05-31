from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path('', views.show_my_name)
]