from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from webapps.e_commerce.models import *



# Create your views here.

 
def index(request, pagename=None):
    context = {}
    if (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):

        return render(request, f'{pagename}.html', context=context)
    return render(request, 'index.html', context=context)



class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "edits.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("home")


def Shop(request):
    return render(request, "shop.html")
