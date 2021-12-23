from django.contrib import admin
from django.urls import path
from .views import say_hello2, main_page

urlpatterns = [
    path('', say_hello2),
    path('main', main_page)
]