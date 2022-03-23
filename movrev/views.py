from django.shortcuts import render, get_object_or_404
from .models import Movie, Review
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'movrev/index.html')

def reviews(request):
    review_list=Review.objects.all()
    return render(request, 'movrev/reviews.html' ,{'review_list' : review_list})

def movies(request):
    movie_list=Movie.objects.all()
    return render(request, 'movrev/movies.html' ,{'movie_list': movie_list})

def moviedetails(request, id):
    movie=get_object_or_404(Movie, pk=id)
    return render(request, 'movrev/moviedetails.html' ,{'movie': movie})
