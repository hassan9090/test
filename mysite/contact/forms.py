from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    

class ContactForm2(forms.Form):
    sender = forms.EmailField()

class ContactForm3(forms.Form):
    message = forms.CharField(widget=forms.Textarea)