from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from webapps.e_commerce.forms import *


def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            htmly = get_template('login.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'okechuquofficial@gmail.com', email
            html_content = htmly.render(d)

            msg = EmailMultiAlternatives(
                subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

            messages.success(
                request, f'Your account has been created!!! Please Login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form, 'title': 'register here'})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Corrected line to log in the user
            messages.success(request, f'Welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'Invalid Credentials, Please Sign Up')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


@login_required(login_url='login')
def Edits(request):
    if request.method == 'POST':
        profile = ProfileUpdate(
            request.POST, request.FILES, instance=request.user.profile)

        if profile.is_valid():
            profile.save()
            messages.success(request, 'Your Profile has been Updated')
            return redirect('home')
    else:
        profile = ProfileUpdate(instance=request.user.profile)

    return render(request, 'edits.htm', {'profile': profile})


def Logout(request):
    try:
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Goodbye')
    except:
        messages.add_message(request, messages.ERROR, 'Try Again')
    return redirect('home')


@login_required(login_url='login')
def Profile(request, user_id):
    if request.method == 'POST':
        profile = ProfileUpdate(
            request.POST, request.FILES, instance=request.user.profile)
        if profile.is_valid():
            profile.save()
            messages.success(request, 'Your Profile has been Updated')
            return redirect('home')
        else:
            profile = ProfileUpdate(instance=request.user.profile)

        user_profile_obj = UserProfile.objects.get(id=user_id)
        user_img = request.FILES['user_img']
        fs_handle = FileSystemStorage()
        img_name = 'images/user_{0}'.format(user_id)

        if fs_handle.exists(img_name):
            fs_handle.delete(img_name)

        fs_handle.save(img_name, user_img)
        user_profile_obj.profile_img = img_name
        user_profile_obj.save()
        user_profile_obj.refresh_from_db()

        return render(request, 'profile.html', {'profile': user_profile_obj})

    if request.user.is_authenticated and request.user.id == user_id:
        user_profile = UserProfile.objects.get(id=user_id)

        return render(request, 'profile.html', {'profile': user_profile})

