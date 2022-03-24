from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.reviews, name='reviews'),
    path('movies/', views.movies, name='movies'),
    path('moviedetails/<int:id>', views.moviedetails, name='moviedetails'),
    path('reviewdetails/<int:id>', views.reviewdetails, name='reviewdetails'),
    path('newmovie/', views.newMovie, name='newmovie'),
    path('newreview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),   
]