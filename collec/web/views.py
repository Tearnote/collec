from django.contrib.auth.models import User
from django.db.models import Q
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
    search_string = request.GET.get('q')
    books = Item.objects.filter(user=user, type='BK')
    if search_string:
        books = books.filter(Q(bookdetails__title__icontains=search_string) |
                             Q(bookdetails__author__icontains=search_string))
    context = {
        'user': user,
        'books': books,
        'search_string': search_string,
    }
    return render(request, 'web/book_list.html', context)


def videogame_list(request, **kwargs):
    username = kwargs['username']
    user = get_object_or_404(User, username=username)
    search_string = request.GET.get('q')
    videogames = Item.objects.filter(user=user, type='VG')
    if search_string:
        videogames = videogames.filter(Q(videogamedetails__title__icontains=search_string))
    context = {
        'user': user,
        'videogames': videogames,
        'search_string': search_string,
    }
    return render(request, 'web/videogame_list.html', context)


def movie_list(request, **kwargs):
    username = kwargs['username']
    user = get_object_or_404(User, username=username)
    search_string = request.GET.get('q')
    movies = Item.objects.filter(user=user, type='MV')
    if search_string:
        movies = movies.filter(Q(moviedetails__title__icontains=search_string))
    context = {
        'user': user,
        'movies': movies,
        'search_string': search_string,
    }
    return render(request, 'web/movie_list.html', context)
