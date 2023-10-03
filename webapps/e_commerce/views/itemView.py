
from django.views.generic import DetailView, View
from webapps.e_commerce.models import *


class ItemDetailView(DetailView):
    model = Item
    template_name = 'detail.html'

