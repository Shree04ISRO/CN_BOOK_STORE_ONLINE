from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
import requests
import json
from .models import Book, Category

def home(request):
    best_sellers = Book.objects.filter(is_best_seller=True)[:6]
    new_arrivals = Book.objects.filter(is_new_arrival=True)[:6]
    audiobooks = Book.objects.filter(is_audiobook=True)[:4]
    categories = Category.objects.all()
    featured = Book.objects.filter(is_best_seller=True).first()
    return render(request, 'books/home.html', {
        'best_sellers': best_sellers,
        'new_arrivals': new_arrivals,
        'audiobooks': audiobooks,
        'categories': categories,
        'featured': featured,
    })

def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    category_filter = request.GET.get('category')
    if category_filter:
        books = books.filter(category__slug=category_filter)
    return render(request, 'books/book_list.html', {
        'books': books,
        'categories': categories,
        'current_category': category_filter,
    })

def books_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'books/book_list.html', {
        'books': books,
        'categories': categories,
        'current_category': slug,
        'category_obj': category,
    })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related = Book.objects.filter(category=book.category).exclude(pk=pk)[:4]
    return render(request, 'books/book_detail.html', {
        'book': book,
        'related_books': related,
    })

def best_sellers(request):
    books = Book.objects.filter(is_best_seller=True)
    return render(request, 'books/book_list.html', {
        'books': books,
        'page_title': '🏆 Best Sellers',
        'categories': Category.objects.all(),
    })

def new_arrivals(request):
    books = Book.objects.filter(is_new_arrival=True)
    return render(request, 'books/book_list.html', {
        'books': books,
        'page_title': '✨ New Arrivals',
        'categories': Category.objects.all(),
    })

def audiobooks(request):
    books = Book.objects.filter(is_audiobook=True)
    return render(request, 'books/book_list.html', {
        'books': books,
        'page_title': '🎧 Audiobooks',
        'categories': Category.objects.all(),
    })

def search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query)
    ) if query else Book.objects.none()
    return render(request, 'books/search_results.html', {
        'books': books,
        'query': query,
        'categories': Category.objects.all(),
    })

def get_ai_summary(request, pk):
    book = get_object_or_404(Book, pk=pk)
    api_key = settings.GEMINI_API_KEY
    
    if api_key == 'YOUR_GEMINI_API_KEY_HERE':
        return JsonResponse({
            'summary': f'"{book.title}" by {book.author} is a captivating read that explores themes relevant to its genre. This book offers readers a unique perspective and has been praised for its engaging narrative and thoughtful insights. Add your Gemini API key in settings.py to get AI-powered summaries!'
        })
    
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"Give a compelling 3-sentence summary of the book '{book.title}' by {book.author}. Focus on what makes it interesting for potential readers."
                }]
            }]
        }
        response = requests.post(url, json=payload, timeout=10)
        data = response.json()
        summary = data['candidates'][0]['content']['parts'][0]['text']
        return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({
            'summary': f'"{book.title}" by {book.author} — {book.description[:200]}...'
        })
