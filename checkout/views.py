from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {        
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MxlzYFfob9hCsSIbUaIjGoskXC9ag5laG7LTfk1gcdr345IopooQmiPxD4ktbfhHpACZhQarfNnu7hnfBFNOa5900LEy5EHdO',
        # 'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
