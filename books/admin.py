from django.contrib import admin

# Register your models here.
from books.models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


class AdminBook(admin.ModelAdmin):
    inlines = [
        ReviewInline
    ]
    list_display = ['title', 'author', 'price']


admin.site.register(Book, AdminBook)
