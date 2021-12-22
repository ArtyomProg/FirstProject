from django.contrib import admin
from django.urls import path
from .views import say_hello, main_page

urlpatterns = [
    path('', say_hello),
    path('main', main_page)
]