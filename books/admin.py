from django.contrib import admin
from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'price', 'is_best_seller', 'is_new_arrival', 'is_audiobook']
    list_filter = ['category', 'is_best_seller', 'is_new_arrival', 'is_audiobook']
    list_editable = ['is_best_seller', 'is_new_arrival', 'price']
    search_fields = ['title', 'author']
    prepopulated_fields = {}
