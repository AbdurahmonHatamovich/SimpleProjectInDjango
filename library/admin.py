from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("id", "last_name", "first_name")


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description30", "price", "count","authors" ,"create_date","comments_count")
    list_display_links = ("title", "description30", "price", "count","authors","comments_count")
    search_fields = ("id", "title")
    ordering = ("id", "title")
    autocomplete_fields = ("authors",)

    def description30(self, obj):
        return obj.description[:20]
    def comments_count(self, obj):
        return obj.comments.all().count()

@admin.register(BookingBook)
class BookingAdmin(ImportExportModelAdmin):
    list_display = ("id","take_date", "return_date")

    # def student(self):
    #     return self.count()
    #
    # def book(self):
    #     return self.count()


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ("id", "text", "student")
