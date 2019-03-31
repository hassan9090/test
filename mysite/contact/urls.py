from django.conf.urls import url
# from django.urls import path
# from . import views
from contact.forms import ContactForm1, ContactForm2, ContactForm3
from contact.views import ContactWizard

app_name = 'contact'

urlpatterns = [
    url('contact/',ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
]
