from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from django.forms import ModelForm, Textarea, HiddenInput,DateInput

from spare.models.garage import Expenses


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'

        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            # 'date_out': DateInput(attrs={'type': 'date'})

            
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['code'].widget.attrs['readonly'] = True
        # self.fields["jobcard"].widget = HiddenInput()  
        