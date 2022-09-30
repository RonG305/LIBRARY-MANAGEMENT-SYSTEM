from django.shortcuts import render, redirect
from django.http import HttpResponse

from books.forms import BookForm
from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    context = {
        'books':Book.objects.all()
    }
    return render(request, 'books/index.html', context)



def add_books(request):
    form =  BookForm  ()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'books/create_books.html', context)

  

def update_books(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'books/update_books.html', context)

def delete_books(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
   
    context = {
        'book': book
    }
    return render(request, 'books/delete_books.html', context)