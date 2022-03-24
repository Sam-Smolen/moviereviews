from django.shortcuts import render, get_object_or_404
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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

def reviewdetails(request, id):
    review=get_object_or_404(Review, pk=id)
    return render(request, 'movrev/reviewdetails.html' ,{'review': review})
@login_required
def newMovie(request):
    form=MovieForm

    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MovieForm()
    else:
        form=MovieForm()
    return render(request, 'movrev/newmovie.html', {'form': form})

def newReview(request):
    form=ReviewForm

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'movrev/newreview.html', {'form': form})

def loginmessage(request):
    return render(request, 'movrev/loginmessage.html')

def logoutmessage(request):
    return render(request, 'movrev/logoutmessage.html')