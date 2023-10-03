from typing import Any, Optional, Sequence, Type, Union
from django import forms
from django.forms.widgets import Widget
from webapps.new_hightech.models.studentModel import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Your Email'}))
    project = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Project'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'w-100 form-control border-0 py-3', 'rows': 6, 'cols': 10, 'placeholder': 'Message'}))


class StudentRegisterForm(forms.ModelForm):
    firstName = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    lastName = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', 'required': 'true'}))
    image = forms.ImageField(label='Profile Picture', widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    studentType = forms.ChoiceField(label='studentType', choices=STUDENT_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', 'required': 'true'}))
    phone = forms.IntegerField(label='Phone Number', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    occupation = forms.CharField(label='Occupation', widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    address = forms.CharField(label='Address', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'required': 'true'}))
    courseOfStudy = forms.ChoiceField(label='Courses of Study', choices=[], widget=forms.Select(
        attrs={'class': 'form-control', 'required': 'true'}))  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically populate the courseOfStudy choices from the queryset
        self.fields['courseOfStudy'].choices = [
            (course.pk, course.courseChoices) for course in Courses.objects.all()]

    class Meta:
        model = StudentsRegisterModel
        fields = ['image', 'firstName', 'lastName', 'gender', 'phone',
                  'occupation', 'email', 'address', 'studentType', 'courseOfStudy']
