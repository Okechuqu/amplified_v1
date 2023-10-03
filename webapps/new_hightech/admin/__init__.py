from django.contrib import admin
from django.http.request import HttpRequest
from webapps.new_hightech.models.FeedbackModel import FeedBack
from webapps.new_hightech.models.title import *
from webapps.new_hightech.models.baseModel import *
from webapps.new_hightech.models.serviceModel import *
from webapps.new_hightech.models.aboutModel import *
from webapps.new_hightech.models.projectModel import *
from webapps.new_hightech.models.staffModel import *
from webapps.new_hightech.models.blogModel import *
from webapps.new_hightech.models.contactModel import *
from webapps.new_hightech.models.testimonialModel import *
from webapps.new_hightech.models.footerModel import *
from webapps.new_hightech.models.privacyModel import *
from webapps.new_hightech.models.termsModel import *
from webapps.new_hightech.models.faqModel import *
from webapps.new_hightech.models.advertModel import *
from webapps.new_hightech.models.studentModel import *
from website.models import Navigations

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'projectName', 'context')
    prepopulated_fields = {'slug': ('projectName',)}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'content')
    prepopulated_fields = {'slug': ('name',)}

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        if About.objects.exists():
            return False
        return True

class TitleAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if TitleModel.objects.exists():
            return False
        return True


class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Footer.objects.exists():
            return False
        return True

class PageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if PageImage.objects.exists():
            return False
        return True

admin.site.register(Fact)
admin.site.register(FAQs)
admin.site.register(Blog)
admin.site.register(Staff)
admin.site.register(Point)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Courses)
admin.site.register(Privacy)
admin.site.register(FeedBack)
admin.site.register(Position)
admin.site.register(Navigations)
admin.site.register(Testimonial)
admin.site.register(Advertisement)
admin.site.register(About, AboutAdmin)
admin.site.register(TermsAndCondition)
admin.site.register(Footer, FooterAdmin)
admin.site.register(PageImage, PageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(StudentsRegisterModel)
admin.site.register(TitleModel, TitleAdmin)
