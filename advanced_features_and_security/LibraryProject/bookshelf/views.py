from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# book_list 
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/delete_book.html', {'book': book})



from django.shortcuts import render
from .forms import ExampleForm
from .models import Book

def form_example_view(request):
    books = Book.objects.all() 
    
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
           
    else:
        form = ExampleForm()

    response = render(request, 'bookshelf/form_example.html', {'form': form, 'books': books})
    
   
    response['Content-Security-Policy'] = "default-src 'self'"
    
    return response