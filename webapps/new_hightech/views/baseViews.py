from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from webapps.new_hightech.forms import *
from webapps.new_hightech.models.FeedbackModel import FeedBack
from webapps.new_hightech.models.serviceModel import Service
from webapps.new_hightech.models.studentModel import *
from webapps.new_hightech.models.projectModel import *


# Create your views here. 


def index(request, pagename=None):
    context = {}
    # context.update(frontendContextProcessor(request))
    if (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):

        return render(request, f'{pagename}.html', context=context)
    return render(request, 'index.html', context=context)


def projectView(request, slug):
    projector = Project.objects.filter(slug=slug)
    template = loader.get_template('project-detail.html')

    context = {
        'projector' : projector
    }

    return HttpResponse(template.render(context, request))


def serviceView(request, slug):
    services = Service.objects.filter(slug=slug)
    template = loader.get_template('service-detail.html')

    context = {
        'services' : services
    }
    return HttpResponse(template.render(context, request))



def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            project = form.cleaned_data['project']
            message = form.cleaned_data['message']

            # Save the data to the ContactFormSubmission model
            submission = FeedBack(name=name, email=email,
                                  project=project, message=message)
            submission.save()
            return render(request, 'index.html')

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


def studentsView(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():

            form.save()

            messages.success(
                request, "You Registration has been recieved, we will contact you through Email!")
            return redirect('index')
        else:
            # Display an error message if the form is not valid
            messages.error(
                request, "Registration failed. Please check your form submission.")
    else:

        form = StudentRegisterForm()
        return render(request, 'students-register.html', {'studentsForm': form})


def searchView(request):
    context = {}
    if request.method == 'POST':
        query = request.POST.get('q')
        projectResults = []
        servicesResults = []
        if query:
            projectResults = Project.objects.filter(projectName__icontains=query)
            servicesResults = Service.objects.filter(name__icontains=query)

        context = {
            'query': query,
            'projectResults': projectResults,
            'servicesResults': servicesResults,
        }

    return render(request, 'search.html', context)
