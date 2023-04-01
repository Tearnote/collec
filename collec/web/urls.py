from django.urls import path, include

from . import views

urlpatterns = [
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('', views.index, name='index'),
    path('<username>/', views.dashboard, name='dashboard'),
    path('<username>/books/', views.book_list, name='book_list'),
    path('<username>/books/detail/', views.book_detail, name='book_detail'),
    path('<username>/books/detail/<int:id>/', views.book_detail, name='book_detail_id'),
    path('<username>/books/delete/<int:id>/', views.book_delete, name='book_delete'),
    path('<username>/videogames/', views.videogame_list, name='videogame_list'),
    path('<username>/movies/', views.movie_list, name='movie_list'),
]
