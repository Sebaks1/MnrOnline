from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import News
from django.urls import reverse

def home(request):
    """
    View function for the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    # Render the home page template 'band/home.html'.
    return render(request, 'band/home.html')


def about(request):
    """
    View function for the about page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered about page.
    """
    # Render the about page template 'band/about.html'.
    return render(request, 'band/about.html')


def contact(request):
    """
    View function for the contact page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered contact page.
    """
    # Render the contact page template 'band/contact.html'.
    return render(request, 'band/contact.html')


def news(request):
    """
    View function for the news page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered news page with a list of news articles.
    """
    # Retrieve all news articles, ordered by date_posted in descending order.
    articles = News.objects.all().order_by('-date_posted')
    
    # Render the news page template 'band/news.html', passing the articles context.
    return render(request, 'band/news.html', {'articles': articles})


def signup(request):
    """
    View function for the signup page.

    Handles user registration and login.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered signup page with a user creation form.
        If the form is valid, redirects to the about page.
    """
    if request.method == 'POST':
        # If the request method is POST, process the submitted form data.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user and log them in automatically.
            user = form.save()
            login(request, user)
            
            # Redirect to the about page after successful signup.
            return redirect(reverse('about'))
    else:
        # If the request method is GET, initialize an empty form.
        form = UserCreationForm()
    
    # Render the signup page template 'band/signup.html', passing the form context.
    return render(request, 'band/signup.html', {'form': form})
