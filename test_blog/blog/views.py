from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

POST = [
    { 'author': 'Anonymous',
    'title': 'Mildsēoc Murka!',
    'content': 'Frēondlīc Murka is here to assisteth thee',
    'date' : '2023',
    },
]

def home(request):
    context = {
        'posts' : POST
    }
    return render(request, 'blog/home.html', context) 

def about(request):
    return render(request, 'blog/about.html')
