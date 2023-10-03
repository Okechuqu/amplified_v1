from django.urls import path
from webapps.oluwa.views import *



urlpatterns = [
    path('', index, name="index"),
    path('<str:pagename>', index, name="index")
]
