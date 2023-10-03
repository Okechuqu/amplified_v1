from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


CATEGORY_CHOICES = (
    ("AP", "appliances"),
    ("FA", "Fabrics"),
    ("LI", "Lighting"),
    ("FU", "furniture"),
    ("BA", "Bath"),
    ("KI", "kitchen"),
)


LABEL_CHOICES = (("P", "primary"), ("S", "secondary"), ("I", "info"), ("D", "danger"))


BADGE_CHOICES = (
    ("OS", "On Sale"),
    ("SO", "Sold Out"),
    ("NA", "New Arrival"),
)


class Item(models.Model):
    price = models.FloatField()
    slug = models.SlugField(default=0)
    title = models.CharField(max_length=100)
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField(default="write a product description")
    pic1 = models.ImageField(blank=True, null=True, upload_to="static/img")
    pic2 = models.ImageField(blank=True, null=True, upload_to="static/img")
    pic3 = models.ImageField(blank=True, null=True, upload_to="static/img")
    badge = models.CharField(blank=True, null=True, choices=BADGE_CHOICES, max_length=2)
    category = models.CharField(
        blank=True, null=True, choices=CATEGORY_CHOICES, max_length=2
    )
    label = models.CharField(blank=True, null=True, choices=LABEL_CHOICES, max_length=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={"slug": self.slug})

    class Meta:
        app_label = 'e_commerce'

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    class Meta:
        app_label = 'e_commerce'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        "BillingAddress", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0.0  # Initialize total as a float
        for order_item in self.items.all():
            final_price = order_item.get_final_price()
            if isinstance(final_price, (int, float)):
                total += final_price
            else:
                # Handle non-numeric values if necessary
                print("Warning: Non-numeric value returned ")
        return total

    class Meta:
        app_label = 'e_commerce'

class Showcase(models.Model):
    title = models.CharField(max_length=100)
    pic1 = models.ImageField(blank=True, null=True, upload_to="static/img")
    category = models.CharField(
        blank=True, null=True, choices=CATEGORY_CHOICES, max_length=2
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        app_label = 'e_commerce'