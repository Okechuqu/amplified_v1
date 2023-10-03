from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from webapps.e_commerce.models import *


PAYMENT_CHOICES = (("S", "Stripe"), ("P", "PayPal"))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.IntegerField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "phone_no",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"placeholder": "Choose a Username"}
        )
        self.fields["first_name"].widget.attrs.update(
            {"placeholder": "Enter Your First Name"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"placeholder": "Enter Your Last Name"}
        )
        self.fields["email"].widget.attrs.update({"placeholder": "Enter Your Email"})
        self.fields["address"].widget.attrs.update(
            {"placeholder": "Enter Your Shipping Address"}
        )
        self.fields["phone_no"].widget.attrs.update(
            {"placeholder": "Enter Your Phone Number"}
        )
        self.fields["password1"].widget.attrs.update(
            {"placeholder": "Create New Password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Re-enter Password"}
        )

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            account = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f" {email} is already in use.")

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        try:
            account = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f" {username} is already taken.")


class ProfileUpdate(forms.Form):
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control-file"})
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )
    address = forms.CharField(max_length=99)

    class Meta:
        model = UserProfile
        fields = ["avatar", "bio", "address"]


class CheckoutForm(forms.Form):
    address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Home Address"})
    )
    address_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter Office Address"}),
    )
    # country = CountryField(blank_label='Select Country').formfield()
    zip = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Zip"}))
    same_billing_address = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )
    save_info = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES
    )


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
