from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html')

def aboutprogram(request):
    return render (request, 'about-program.html')