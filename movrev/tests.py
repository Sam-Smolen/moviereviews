from django.test import TestCase
from .models import Movie, Review
import datetime

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