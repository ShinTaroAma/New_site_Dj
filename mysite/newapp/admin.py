from django.contrib import admin
from .models import Author, Book, Person, NewStoreBooks

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(NewStoreBooks)
admin.site.register(Person)
