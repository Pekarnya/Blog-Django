"""
urls defined with django.urls.path
path('', views.page_name, views.name, name)
"""
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.home, name='blog-home'),
    path('home', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
    path('register/', views.register_page, name='blog-register'),
    path('goods/', views.goods, name='blog-goods'),
    path('godown/', views.godown, name='blog-godown'),
    path('contacts/', views.contacts, name='blog-contacts'),
    path('check/', views.login, name='blog-check'),
    path('logout/', views.logout, name='blog-logout'),
    path('welcome/', views.welcome_page, name='blog-welcome'),
    path('profile/', views.profile, name='blog-profile'),
    path('profile/', include('actstream.urls')),
]
