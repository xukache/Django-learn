from django.contrib import admin
from .models import Book, Person


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'read', 'comment']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'book']



admin.site.register(Book, BookAdmin)
admin.site.register(Person, PersonAdmin)