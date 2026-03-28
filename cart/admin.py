from django.contrib import admin
from .models import CartItem, Order

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['book', 'quantity', 'added_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'total_amount', 'created_at', 'is_paid']
    list_filter = ['is_paid']
