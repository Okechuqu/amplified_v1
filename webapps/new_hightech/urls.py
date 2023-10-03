from django.urls import re_path as url
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings
from webapps.new_hightech.views.baseViews import *


urlpatterns = [
    path('', index, name='index'),
    path('search/', searchView, name='search'),
    path('<str:pagename>', index, name='index'),
    path('feedback/', contactView, name='feedback'),
    path('students-register/', studentsView, name='registration'),
    path('service-detail/<slug:slug>', serviceView, name='service-detail'),
    path('project-detail/<slug:slug>', projectView, name='project-detail'),
]
 