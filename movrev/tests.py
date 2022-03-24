from django.test import TestCase
from .models import Movie, Review
import datetime
from .forms import MovieForm, ReviewForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MovieTest(TestCase):
    def setup(self):
        movie=Movie(movietitle='Ace Ventura Pet Detective', movreleasedate='1994/02/04', movgenre='Comedy/Mystery')
        return movie

    def test_movietable(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')

    def test_titlestring(self):
        movie=self.setup()
        self.assertEqual(str(movie.movietitle), 'Ace Ventura Pet Detective')
    
    def test_releasedate(self):
        movie=self.setup()
        self.assertEqual(str(movie.movreleasedate), '1994/02/04')

    def test_movgenre(self):
        movie=self.setup()
        self.assertEqual(str(movie.movgenre), 'Comedy/Mystery')

class ReviewTest(TestCase):
    def setup(self):
        review=Review(reviewdate='2022/03/22', review='Funny movie. Jim Carrey did a great job, Would recommend to a friend.', movieid_id='1')
        return review

    def test_reviewtable(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

    def test_reviewdate(self):
        review=self.setup()
        self.assertEqual(str(review.reviewdate), '2022/03/22')
    
    def test_review(self):
        review=self.setup()
        self.assertEqual(str(review.review), 'Funny movie. Jim Carrey did a great job, Would recommend to a friend.')

    def test_movieid(self):
        review=self.setup()
        self.assertEqual(str(review.movieid_id), '1')

class New_Movie_Authentification_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='testuser1', password='p@ssw0rd1')
        self.movie=Movie.objects.create(movietitle='Ace Ventura Pet Detective',movreleasedate='1994/02/04',movgenre='Comedy/Mystery')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmovie'))
        self.assertRedirects(response, '/accounts/login/?next=/movrev/newmovie/')