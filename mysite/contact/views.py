from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from formtools.wizard.views import SessionWizardView
from django.core import mail
import logging

logr = logging.getLogger(__name__)

class ContactWizard(SessionWizardView):
    template_name = 'contact_form.html'

    def done(self,form_list,**kwargs):
        from_data = process_form_data(form_list)
        return render_to_response('done.html',{'form_date':from_data})

def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]

    logr.debug(form_data[0]['subject'])
    return form_data