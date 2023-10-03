from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from webapps.e_commerce.forms import *


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                address = form.cleaned_data.get('address')
                address_2 = form.cleaned_data.get('address_2')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                # TODO: add functionality for these fields
                # same_billing_address = form.cleaned_data.get(
                #     'same_billing_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user=self.request.user,
                    address=address,
                    address_2=address_2,
                    country=country,
                    zip=zip,
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                # TODO: add a redirect to the selected payment option
                return redirect('checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, 'No Orders Yet')
            return redirect('cart')

        context = {
            'form': form
        }
        return render(self.request, 'checkout.html', context)


class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'payment.html')


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()

            # Process payment based on the selected payment method
            if payment.payment_method == 'credit_card':
                # Process credit card payment
                # Add your credit card payment processing code here

                pass
            elif payment.payment_method == 'paypal':
                # Process PayPal payment
                # Add your PayPal payment processing code here
                pass
            elif payment.payment_method == 'bank_transfer':
                # Process bank transfer payment
                # Add your bank transfer payment processing code here
                pass

            return render(request, 'success.html', {'payment': payment})
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})

