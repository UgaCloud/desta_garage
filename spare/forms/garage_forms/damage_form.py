from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from django.forms import ModelForm, Textarea, HiddenInput,DateInput

from spare.models.garage import Damage


class DamageForm(forms.ModelForm):
    class Meta:
        model = Damage
        fields = '__all__'

        # widgets = {
        #     'date_in': DateInput(attrs={'type': 'date'}),
        #     'date_out': DateInput(attrs={'type': 'date'})

            
        # }

    def __init__(self, *args, **kwargs):
        super(DamageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['code'].widget.attrs['readonly'] = True
        self.fields["jobcard"].widget = HiddenInput()  
        