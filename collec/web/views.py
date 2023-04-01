from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from collec.web.forms import BookForm
from collec.web.models import Item


def index(request):
    return render(request, 'web/index.html')


def dashboard(request, **kwargs):
    username = kwargs['username']
    url_user = get_object_or_404(User, username=username)
    books = Item.objects.filter(user=url_user, type='BK')
    videogames = Item.objects.filter(user=url_user, type='VG')
    movies = Item.objects.filter(user=url_user, type='MV')
    context = {
        'url_user': url_user,
        'books': books,
        'videogames': videogames,
        'movies': movies,
    }
    return render(request, 'web/dashboard.html', context)


def book_list(request, **kwargs):
    username = kwargs['username']
    url_user = get_object_or_404(User, username=username)
    search_string = request.GET.get('q')
    sort_mode = request.GET.get('sort')
    if sort_mode is None:
        sort_mode = 'modified'
    if sort_mode != 'modified' and sort_mode != 'created':
        sort_mode_arg = 'bookdetails__' + sort_mode
    else:
        sort_mode_arg = '-' + sort_mode
    books = Item.objects.filter(user=url_user, type='BK').order_by(sort_mode_arg)
    if search_string:
        books = books.filter(Q(bookdetails__title__icontains=search_string) |
                             Q(bookdetails__author__icontains=search_string))
    context = {
        'url_user': url_user,
        'books': books,
        'search_string': search_string,
        'sort_mode': sort_mode,
    }
    return render(request, 'web/book_list.html', context)


def book_detail(request, **kwargs):
    if request.method == 'GET':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        context = {
            'url_user': url_user,
            'form': BookForm(),
        }
        return render(request, 'web/detail_base.html', context)

    if request.method == 'POST':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        form = BookForm(data=request.POST)
        item = Item()
        item.user = url_user
        item.type = 'BK'
        form.instance.item = item
        if form.is_valid():
            item.save()
            form.save()

        return redirect('book_list', username=username)


def videogame_list(request, **kwargs):
    username = kwargs['username']
    url_user = get_object_or_404(User, username=username)
    search_string = request.GET.get('q')
    sort_mode = request.GET.get('sort')
    if sort_mode is None:
        sort_mode = 'modified'
    if sort_mode != 'modified' and sort_mode != 'created':
        sort_mode_arg = 'videogamedetails__' + sort_mode
    else:
        sort_mode_arg = '-' + sort_mode
    videogames = Item.objects.filter(user=url_user, type='VG').order_by(sort_mode_arg)
    if search_string:
        videogames = videogames.filter(Q(videogamedetails__title__icontains=search_string))
    context = {
        'url_user': url_user,
        'videogames': videogames,
        'search_string': search_string,
        'sort_mode': sort_mode,
    }
    return render(request, 'web/videogame_list.html', context)


def movie_list(request, **kwargs):
    username = kwargs['username']
    url_user = get_object_or_404(User, username=username)
    search_string = request.GET.get('q')
    sort_mode = request.GET.get('sort')
    if sort_mode is None:
        sort_mode = 'modified'
    if sort_mode != 'modified' and sort_mode != 'created':
        sort_mode_arg = 'moviedetails__' + sort_mode
    else:
        sort_mode_arg = '-' + sort_mode
    movies = Item.objects.filter(user=url_user, type='MV').order_by(sort_mode_arg)
    if search_string:
        movies = movies.filter(Q(moviedetails__title__icontains=search_string))
    context = {
        'url_user': url_user,
        'movies': movies,
        'search_string': search_string,
        'sort_mode': sort_mode,
    }
    return render(request, 'web/movie_list.html', context)
