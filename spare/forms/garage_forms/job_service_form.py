from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from django.forms import ModelForm, Textarea, HiddenInput,DateInput

from spare.models.garage import JobCardService


class JobServiceForm(forms.ModelForm):
    class Meta:
        model = JobCardService
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(JobServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['code'].widget.attrs['readonly'] = True
        # self.fields["jobcard"].widget = HiddenInput()  
        