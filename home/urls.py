# home/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.about, name='home'),  # Set signup view as homepage
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('news/', views.news, name='news'),
    path('login/', auth_views.LoginView.as_view(template_name='band/login.html'), name='login'),
]


