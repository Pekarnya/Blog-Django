"""_summary_ Rendering DOM
Returns:
    _type_: DOM object
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

POST = [
    {'author': 'Anonymous', 'title': 'Mildsēoc Murka!',
     'content': 'Frēondlīc Murka is here to assisteth thee',
     'date': '2023'},
]


def register_page(request):
    """Create a new profile from POST request
    posting unique identifier

    Args:
        request (POST): POST request from submit form

    Returns:
        User.objects.create_user: add user data to the database
        Profile.objects.create: Creates new profile
    """

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('blog-register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('blog-register')
            else:
                messages.info(request, message=f"Welcome {username}")
                user = User.objects.create_user(username=username,
                                                email=email, password=pass1)
                user.save()

                # login user and redirect

                # create Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,
                                                     id=user_model.id)
                new_profile.save()
                return redirect('blog-login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('blog-register')

    else:
        return render(request, template_name='blog/login.html')


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


def goods(request):
    """Post method with list of merchendise

    Args:
        request (Any): get request

    returns:
        _type_: goods.html
    """
    return render(request, 'blog/goods.html')


def godown(request):
    """Render a godown page

    Args: request (Any): get request

    returns:
        _type_: godown.html
    """
    return render(request, 'blog/godown.html')


def contacts(request):
    """Render a contact page

    Args: request (Any): get request

    returns:
        _type_: contacts.html
    """
    return render(request, 'blog/contacts.html')
