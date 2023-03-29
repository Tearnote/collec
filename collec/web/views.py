from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from collec.web.models import Item


def index(request):
    return render(request, 'web/index.html')


def dashboard(request, **kwargs):
    username = kwargs['username']
    user = get_object_or_404(User, username=username)
    books = Item.objects.filter(user=user, type='BK')
    videogames = Item.objects.filter(user=user, type='VG')
    movies = Item.objects.filter(user=user, type='MV')
    context = {
        'user': user,
        'books': books,
        'videogames': videogames,
        'movies': movies,
    }
    return render(request, 'web/dashboard.html', context)


def book_list(request, **kwargs):
    username = kwargs['username']
    user = get_object_or_404(User, username=username)
    books = Item.objects.filter(user=user, type='BK')
    context = {
        'user': user,
        'books': books,
    }
    return render(request, 'web/book_list.html', context)
