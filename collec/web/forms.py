from django import forms

from collec.web.models import BookDetails, VideogameDetails, MovieDetails


class BookForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = ('title', 'author', 'owned')


class VideogameForm(forms.ModelForm):
    class Meta:
        model = VideogameDetails
        fields = ('title', 'platform', 'owned')


class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieDetails
        fields = ('title', 'owned')
