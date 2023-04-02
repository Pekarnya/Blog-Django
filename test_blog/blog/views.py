"""_summary_ Rendering DOM
Returns:
    _type_: DOM object
"""
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.shortcuts import  render
from .forms import NewUserForm
from django.contrib import messages
# Create your views here.

POST = [
    {'author': 'Anonymous',
    'title': 'Mildsēoc Murka!',
    'content': 'Frēondlīc Murka is here to assisteth thee',
    'date' : '2023',
    },
]


def register_page(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        user = form.save()
        login(request, user)
        messages.success(request, 'You`re welcome!')
        return redirect('')
        # messages.error(request, 'You gave us wrong info don`t you?')
        # form.save()
    
    form = NewUserForm()
    return render(request=request, template_name='blog/login.html')


def home(request):
    """Getting start page

    Args:
        request (Any): variable before showing the page*************

    Returns:
        _type_: _description_
    """
    context = {
        'posts': POST
    }
    return render(request, 'blog/home.html', context) 


def about(request):
    """About page improovements required"""
    return render(request, 'blog/about.html')


def login(request):
    """Using post method for authentication

    Args:
        request (Any): _description_

    Returns:
        _type_: login.html
    """
    return render(request, 'blog/login.html')
