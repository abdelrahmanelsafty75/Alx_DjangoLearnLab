from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

from rest_framework import filters  # Search and Ordering
from django_filters import rest_framework as django_filters  # Filtering
# Create your views here.

#ListView
class BookListview(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
         django_filters.DjangoFilterBackend]
    
    filterset_fields = ['title', 'author', 'published_date'] 
    search_fields = ['title', 'publication_year']
    ordering_fields = ['publication_year', 'title'] 
    ordering = ['title']  

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # This method is called when a new book is being created.
        # It allows us to customize the creation process, such as associating the book with an author.
        # For example, if we want to automatically associate the book with a specific author, we could do something like this:
        # author = Author.objects.get(id=self.request.data.get('author_id'))
        # serializer.save(author=author)
        serializer.save()
    
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):
        # This method is called when an existing book is being updated.
        # Similar to perform_create, we can customize the update process here.
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]