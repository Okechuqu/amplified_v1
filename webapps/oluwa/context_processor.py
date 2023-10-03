from webapps.oluwa.models import *
from webapps.oluwa.forms import *


def frontendContextProcessor(request):
    return{ 
        'siteInfo' : SiteInfoModel.objects.all(),
        'contacts' : ContactInfo.objects.all(),
        'soldiers' : Soldier.objects.all(),
        'events' : Event.objects.all(),
        'mission' : Mission.objects.all(),
        'press' : PressRelease.objects.all(),
    }
