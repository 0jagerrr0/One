from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)