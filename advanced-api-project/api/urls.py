from django.urls import  include, path
from . import views
#from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api-token-auth/',include('rest_framework.urls')),  # This line includes the default login/logout views for the browsable API.
    
    path('books/', views.BookListview.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]