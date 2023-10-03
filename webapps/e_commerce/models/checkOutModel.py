from django.db import models
from django.conf import settings


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    # country = CountryField(multiple=False)
    zip = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        app_label = 'e_commerce'

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("credit_card", "Credit Card"),
        ("paypal", "PayPal"),
        ("bank_transfer", "Bank transfer"),
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    cvv = models.CharField(max_length=3, null=True, blank=True)
    expiration_month = models.CharField(max_length=2, null=True, blank=True)
    expiration_year = models.CharField(max_length=4, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=11, null=True, blank=True)
    routing_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Payment - {self.payment_method}"

    class Meta:
        app_label = 'e_commerce'