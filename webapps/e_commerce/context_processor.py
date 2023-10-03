from webapps.e_commerce.models import *
from webapps.e_commerce.forms import *


def frontendContextProcessor(request):
    return{
        'billingAddress' : BillingAddress.objects.all(),
        'userProfile' : UserProfile.objects.all(),
        'orderItems' : OrderItem.objects.all(),
        'showcase' : Showcase.objects.all(),
        'payments' : Payment.objects.all(),
        'orders': Order.objects.all(),
        'items' : Item.objects.all(),
        # 'userRegister' : UserRegisterForm,
        # 'profileUpdate' : ProfileUpdate,
        # 'checkOutForm' : CheckoutForm,
        # 'payments' : PaymentForm,
    }