from django.urls import path
from .views import BooksListView,BooksDetailView

urlpatterns = [
    path('library/', BooksListView.as_view(), name='library'),
    path('<int:id>', BooksDetailView.as_view(), name='book-detail')
]