from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request=request, template_name="index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")