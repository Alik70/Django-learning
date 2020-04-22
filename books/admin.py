from django.contrib import admin

# Register your models here.
from books.models import Book


class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']


admin.site.register(Book, AdminBook)
