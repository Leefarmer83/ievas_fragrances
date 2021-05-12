from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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
        'stripe_public_key': 'pk_test_51IqFj9IHiObbQ8fC7uq4fDv3xLtfQEHY1lPDmn7irAgWlTdywkR0brQf4ceyvrQyS0lvXc1lr8Rk12Ef32H9DamO0011EF8ayV',
        'client_seceret': 'test client secret',
    }

    return render(request, template, context)