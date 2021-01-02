from django.forms import ModelForm
from .models import Movie, Review


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['content', 'year']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content']
