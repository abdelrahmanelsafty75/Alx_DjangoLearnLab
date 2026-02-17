from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book ,Library, Librarian
from django.views.generic import DetailView
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
