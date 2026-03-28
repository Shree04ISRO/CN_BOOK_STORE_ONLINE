from django.db import models
from books.models import Book

class CartItem(models.Model):
    session_key = models.CharField(max_length=40)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} ({self.quantity})"

    @property
    def total_price(self):
        return self.book.price * self.quantity

class Order(models.Model):
    session_key = models.CharField(max_length=40)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk} - {self.full_name}"
