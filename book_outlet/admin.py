from django.contrib import admin
from .models import Book

# Register your models here.
class Bookadmin(admin.ModelAdmin):
  list_filter = ("author","rating",)
  list_display = ("author","title","rating")


admin.site.register(Book,Bookadmin)