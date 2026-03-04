from rest_framework import serializers
from .models import Book, Author
import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def validate_publication_year(self, value):
        current_date = datetime.date.today().year
        if value > current_date:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested Serializer: This dynamically serializes all books related to this author.
    # The variable name 'books' must match the 'related_name' defined in the Book model's ForeignKey.
    # We use many=True because one author can have multiple books, and read_only=True to prevent complex creation logic.
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']