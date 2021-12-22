from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
	return render(request, "index.html")

def main_page(request):
	return render(request, "main.html")	