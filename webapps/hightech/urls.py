from django.urls import re_path as url
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings

from webapps.hightech.views import index

urlpatterns = [
    path('', index, name='index'),
]
