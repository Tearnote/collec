from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<username>/', views.dashboard, name='dashboard'),
    path('<username>/books/', views.book_list, name='book_list'),
    path('<username>/books/detail/', views.book_detail, name='book_detail'),
    path('<username>/books/detail/<int:id>/', views.book_detail, name='book_detail_id'),
    path('<username>/books/delete/<int:id>/', views.book_delete, name='book_delete'),
    path('<username>/videogames/', views.videogame_list, name='videogame_list'),
    path('<username>/videogames/detail/', views.videogame_detail, name='videogame_detail'),
    path('<username>/videogames/detail/<int:id>/', views.videogame_detail, name='videogame_detail_id'),
    path('<username>/videogames/delete/<int:id>/', views.videogame_delete, name='videogame_delete'),
    path('<username>/movies/', views.movie_list, name='movie_list'),
    path('<username>/movies/detail/', views.movie_detail, name='movie_detail'),
    path('<username>/movies/detail/<int:id>/', views.movie_detail, name='movie_detail_id'),
    path('<username>/movies/delete/<int:id>/', views.movie_delete, name='movie_delete'),
]
