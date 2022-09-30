
from django import forms
from  .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_code',
            'book_name',
            'author_name',
            'date',
            'status'

        ]

        labels = {
            'book_code': 'Book code',
            'book_name': 'Book name',
            'author_name': 'Author name',
            'date': 'Date posted',
            'status': 'Status'
        }

        widgets = {
            'book_code': forms.TextInput(attrs={'class':'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'})

        }