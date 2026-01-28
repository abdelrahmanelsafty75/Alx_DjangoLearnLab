# Create Book Record

from bookshelf.models import Book
book1 = Book(title="1984", author="George Orwell", publication_year=1949)
book1.save()

## Retrieve Book Record

from bookshelf.models import Book

# Retrieve the book using objects.get
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

Book.objects.all()

# Update Book Record

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title

## Delete Book Record


from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()