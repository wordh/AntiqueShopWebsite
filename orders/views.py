from django.urls import reverse
import time
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from carts.models import Cart

from .models import Oder


def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    new_order, created = Oder.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()
    if new_order.status == "Finish":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
    context = {}
    template = "products/home.html"
    return render(request, template, context)