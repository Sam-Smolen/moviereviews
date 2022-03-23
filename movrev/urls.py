from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.reviews, name='reviews'),
    path('movies/', views.movies, name='movies'),
    path('moviedetails/<int:id>', views.moviedetails, name='moviedetails'),   
]