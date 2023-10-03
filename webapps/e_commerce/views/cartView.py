from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from webapps.e_commerce.models import *



class CartView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            orders = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'orders': orders
            }
            return render(self.request, 'cart.html', context)

        except ObjectDoesNotExist:
            messages.error(self.request, 'No Orders Yet')
            return redirect('/')



@login_required(login_url='login')
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Successfuly Updated')
            return redirect('home')

        else:
            order.items.add(order_item)
            messages.info(request, 'Successfuly Added')
            return redirect('home')

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'Successfuly Added')
        return redirect('home')


@login_required(login_url='login')
def add_single_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Successfuly Updated')
            return redirect('Cart')

        else:
            order.items.add(order_item)
            messages.info(request, 'Successfuly Added')
            return redirect('detail', slug=slug)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'Successfuly Added')
        return redirect('detail', slug=slug)


@login_required(login_url='login')
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, 'Removed')
            return redirect('cart', slug=slug)

        else:
            messages.info(request, 'Not in Cart')
            return redirect('detail', slug=slug)
    else:
        messages.info(request, 'No active Orders')
        return redirect('detail', slug=slug)


@login_required(login_url='login')
def remove_single_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, 'Updated')
            return redirect('Cart')

        else:
            messages.info(request, 'Not in Cart')
            return redirect('detail', slug=slug)
    else:
        messages.info(request, 'No active Orders')
        return redirect('detail', slug=slug)

