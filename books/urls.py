from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/category/<slug:slug>/', views.books_by_category, name='books_by_category'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('best-sellers/', views.best_sellers, name='best_sellers'),
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),
    path('audiobooks/', views.audiobooks, name='audiobooks'),
    path('search/', views.search, name='search'),
    path('api/book-summary/<int:pk>/', views.get_ai_summary, name='get_ai_summary'),
]
