from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from collec.web.forms import BookForm, VideogameForm, MovieForm
from collec.web.models import Item


def index(request):
    return render(request, 'web/index.html')


def dashboard(request, **kwargs):
    username = kwargs['username']
    url_user = get_object_or_404(User, username=username)
    books = Item.objects.filter(user=url_user, type='BK').order_by('-modified')[:5]
    videogames = Item.objects.filter(user=url_user, type='VG').order_by('-modified')[:5]
    movies = Item.objects.filter(user=url_user, type='MV').order_by('-modified')[:5]
    context = {
        'url_user': url_user,
        'books': books,
        'videogames': videogames,
        'movies': movies,
        'own_user': url_user == request.user,
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
        'own_user': url_user == request.user,
    }
    return render(request, 'web/book_list.html', context)


def book_detail(request, **kwargs):
    if request.method == 'GET':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        if 'id' in kwargs:
            item = get_object_or_404(Item, id=kwargs['id'])
            form = BookForm(instance=item.bookdetails)
        else:
            form = BookForm()
        context = {
            'url_user': url_user,
            'form': form,
            'new': 'id' not in kwargs,
        }
        if not context['new']:
            context['id'] = kwargs['id']
        return render(request, 'web/book_detail.html', context)

    if request.method == 'POST':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        if 'id' in kwargs:
            item = get_object_or_404(Item, id=kwargs['id'])
            form = BookForm(instance=item.bookdetails, data=request.POST)
        else:
            item = Item()
            item.user = url_user
            item.type = 'BK'
            form = BookForm(data=request.POST)
            form.instance.item = item
        if form.is_valid():
            item.save()
            form.save()

        return redirect('book_list', username=username)


def book_delete(request, **kwargs):
    username = kwargs['username']
    if request.method != 'POST':
        return redirect('book_list', username=username)

    url_user = get_object_or_404(User, username=username)
    id = kwargs['id']
    item = get_object_or_404(Item, id=id)
    item.delete()
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
        'own_user': url_user == request.user,
    }
    return render(request, 'web/videogame_list.html', context)


def videogame_detail(request, **kwargs):
    if request.method == 'GET':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        if 'id' in kwargs:
            item = get_object_or_404(Item, id=kwargs['id'])
            form = VideogameForm(instance=item.videogamedetails)
        else:
            form = VideogameForm()
        context = {
            'url_user': url_user,
            'form': form,
            'new': 'id' not in kwargs,
        }
        if not context['new']:
            context['id'] = kwargs['id']
        return render(request, 'web/videogame_detail.html', context)

    if request.method == 'POST':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        if 'id' in kwargs:
            item = get_object_or_404(Item, id=kwargs['id'])
            form = VideogameForm(instance=item.videogamedetails, data=request.POST)
        else:
            item = Item()
            item.user = url_user
            item.type = 'VG'
            form = VideogameForm(data=request.POST)
            form.instance.item = item
        if form.is_valid():
            item.save()
            form.save()

        return redirect('videogame_list', username=username)


def videogame_delete(request, **kwargs):
    username = kwargs['username']
    if request.method != 'POST':
        return redirect('videogame_list', username=username)

    url_user = get_object_or_404(User, username=username)
    id = kwargs['id']
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('videogame_list', username=username)


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
        'own_user': url_user == request.user,
    }
    return render(request, 'web/movie_list.html', context)


def movie_detail(request, **kwargs):
    if request.method == 'GET':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        if 'id' in kwargs:
            item = get_object_or_404(Item, id=kwargs['id'])
            form = MovieForm(instance=item.moviedetails)
        else:
            form = MovieForm()
        context = {
            'url_user': url_user,
            'form': form,
            'new': 'id' not in kwargs,
        }
        if not context['new']:
            context['id'] = kwargs['id']
        return render(request, 'web/movie_detail.html', context)

    if request.method == 'POST':
        username = kwargs['username']
        url_user = get_object_or_404(User, username=username)
        if 'id' in kwargs:
            item = get_object_or_404(Item, id=kwargs['id'])
            form = MovieForm(instance=item.moviedetails, data=request.POST)
        else:
            item = Item()
            item.user = url_user
            item.type = 'MV'
            form = MovieForm(data=request.POST)
            form.instance.item = item
        if form.is_valid():
            item.save()
            form.save()

        return redirect('movie_list', username=username)


def movie_delete(request, **kwargs):
    username = kwargs['username']
    if request.method != 'POST':
        return redirect('movie_list', username=username)

    url_user = get_object_or_404(User, username=username)
    id = kwargs['id']
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('movie_list', username=username)
