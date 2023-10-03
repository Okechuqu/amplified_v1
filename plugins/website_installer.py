
import os
from decouple import config
from django.conf import settings
from website.models.webtemplates import WebTemplate
from plugins.sqlite import databaseWebsiteStorageDB


def webInstaller():
    try:
        w = WebTemplate.objects.all()
        if w.exists():
            checker = w[0]
            databaseWebsiteStorageDB(name=checker.name, path=checker.path)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
