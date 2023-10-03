from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth
from webapps.e_commerce.views import *


urlpatterns = [
    path("", index, name="index"),
    path("shop/", Shop, name="shop"),
    path("login/", Login, name="login"),
    path("accounts/", include("allauth.urls")),
    path("<str:pagename>", index, name="index"),
    path("register/", Register, name="register"),
    path("cart/", CartView.as_view(), name="Cart"),
    path("edits/<int:user_id>", Edits, name="edits"),
    path("profile/<int:user_id>", Profile, name="profile"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("detail/<slug>/", ItemDetailView.as_view(), name="detail"),
    path("payment/<payment_option>", PaymentView.as_view(), name="payment"),
    path("remove-from-cart/<slug>/", remove_from_cart, name="remove-from-cart"),
    path("password-change/", ChangePasswordView.as_view(), name="password_change"),
    path("add-single-to-cart/<slug>/", add_single_to_cart, name="add-single-to-cart"),
    path("logout/", auth.LogoutView.as_view(template_name="home.html"), name="logout"),
    path(
        "remove-single-from-cart/<slug>/",
        remove_single_from_cart,
        name="remove-single-from-cart",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
