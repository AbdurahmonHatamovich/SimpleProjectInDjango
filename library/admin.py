from django.contrib import admin
from .models import Book, Author,BookingBook,Comments

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookingBook)
admin.site.register(Comments)
