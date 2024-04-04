from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name")

@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ("id", "text", "student")


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description", "price", "count", "create_date")
    list_display_links = ("title", "description", "price", "count")
    search_fields = ("id", "title")
    ordering = ("id", "title")


@admin.register(BookingBook)
class BookingAdmin(ImportExportModelAdmin):
    list_display = ("id", "student", "book", "take_date", "return_date")

    def student(self):
        return self.count()

    def book(self):
        return self.count()
