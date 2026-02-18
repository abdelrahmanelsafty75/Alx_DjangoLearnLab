from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class RegisterView(CreateView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

#UserCreationForm() is a built-in form provided by Django that handles user registration. It includes fields for username, password, and password confirmation, along with validation to ensure that the passwords match and meet certain criteria. By using this form, you can easily create a registration page for new users without having to manually define the form fields and validation logic.