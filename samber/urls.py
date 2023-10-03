from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from plugins.contextManager import update_templates
from plugins.website_installer import webInstaller
from .api import api

VERSION = "v1"

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls',
    #      'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),

    # this will set the selected app with url pattern
    path('', include(f"{settings.WEBSITE_URL}")),

    path('api/', api.urls),

    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
# this will register the activated webapp and save to sqlit db
webInstaller()
update_templates()
# print(settings.TEMPLATES)

