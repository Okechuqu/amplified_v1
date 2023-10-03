from webapps.new_hightech.models import *
from webapps.new_hightech.forms import *
from website.models import Navigations

def frontendContextProcessor(request):
    return {
        'testimonial': Testimonial.objects.all(),
        'terms': TermsAndCondition.objects.all(),
        'adverts': Advertisement.objects.all(),
        'pageImage' : PageImage.objects.all(),
        'titles': TitleModel.objects.all(),
        'projects': Project.objects.all(),
        'contacts': Contact.objects.all(),
        'services': Service.objects.all(), 
        'personel': Staff.objects.all(),
        'sliders': Slider.objects.all(),
        'privacy':Privacy.objects.all(),
        'footer': Footer.objects.all(),
        'abouts': About.objects.all(),
        'facts': Fact.objects.all(),
        'blogs': Blog.objects.all(),
        'faqs': FAQs.objects.all(),
        "navigation":Navigations.objects.all().order_by('order'),
        'studentsForm': StudentRegisterForm,
        'form': ContactForm,
        
    } 
