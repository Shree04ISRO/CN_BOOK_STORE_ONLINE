from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from books.models import Book
from .models import CartItem, Order

def _get_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def cart_view(request):
    session_key = _get_session(request)
    items = CartItem.objects.filter(session_key=session_key).select_related('book')
    total = sum(item.total_price for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    session_key = _get_session(request)
    item, created = CartItem.objects.get_or_create(session_key=session_key, book=book)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'"{book.title}" added to cart!')
    return redirect(request.META.get('HTTP_REFERER', 'cart'))

def remove_from_cart(request, pk):
    session_key = _get_session(request)
    CartItem.objects.filter(session_key=session_key, pk=pk).delete()
    return redirect('cart')

def update_cart(request, pk):
    session_key = _get_session(request)
    item = get_object_or_404(CartItem, pk=pk, session_key=session_key)
    qty = int(request.POST.get('quantity', 1))
    if qty > 0:
        item.quantity = qty
        item.save()
    else:
        item.delete()
    return redirect('cart')

def checkout(request):
    session_key = _get_session(request)
    items = CartItem.objects.filter(session_key=session_key).select_related('book')
    total = sum(item.total_price for item in items)
    
    if not items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart')
    
    if request.method == 'POST':
        order = Order.objects.create(
            session_key=session_key,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            total_amount=total,
            is_paid=True,
        )
        CartItem.objects.filter(session_key=session_key).delete()
        return redirect('order_success', order_id=order.pk)
    
    return render(request, 'cart/checkout.html', {'items': items, 'total': total})

def order_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'cart/order_success.html', {'order': order})
