from django import forms

from collec.web.models import BookDetails


class BookForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = ('title', 'author', 'owned')
