from django.shortcuts import redirect
from django.contrib import messages
from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            _, created = Subscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, '🎉 You\'ve successfully subscribed to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed!')
    return redirect(request.META.get('HTTP_REFERER', 'home'))
