from typing import Any, Dict, List, Optional, Type
from django.contrib import admin
from django.http import JsonResponse
from django.contrib.admin.views.main import ChangeList
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
from django.urls.resolvers import URLPattern
from django.urls import path, include
from plugins.website_handler import webDirectory
from website.models import *
import os
import json
#


@admin.register(WebTemplate)
class WebsitesAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def get_urls(self) -> List[URLPattern]:
        urls = super().get_urls()
        extra_url = [
            path('register-website', self.register_website,
                 name='register-website')
        ]
        return urls + extra_url

    def register_website(self, request):
        message = ''
        data = json.loads(request.body)
        data_converted = int(data.get('is_activated'))
        data['is_activated'] = data_converted

        m = self.model.objects.all()

        if m.exists():
            d = m[0]
            # if is true= activate template
            if data.get('is_activated') == 1:
                m.filter(id=d.id).update(**data)

            # if is false= deactivate web template
            elif data.get('is_activated') == 0:
                m.filter(id=d.id).delete()

            elif data.get('is_activated') == 'delete':
                #  apply the delete code
                print('deleted')

        else:
            m.create(**data)

        message = data.get('message')
        return JsonResponse({'message': message})

    def changelist_view(self, request, extra_context={}):
        container = []
        # Update the extra_context dictionary with your custom data
        modell = self.model.objects.all()
        data_model = modell[0] if modell.exists() else []

        website_directory_path = webDirectory()
        for directory in website_directory_path:

            if os.path.exists(f"{directory}/manifest.json"):

                manifest = open(f"{directory}/manifest.json").read()
                data = eval(manifest)
                data['app'] = f"{directory}"
                container.append(data)
            else:
                pass

        # extend context data
        extra_context['webapps'] = container
        extra_context['web_template_installed'] = data_model if len(modell) > 0 else 'DEFAULT TEMPLATE ACTIVATED.'
            

        return super().changelist_view(request, extra_context=extra_context)
