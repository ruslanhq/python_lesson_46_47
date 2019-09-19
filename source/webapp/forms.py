from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label='Status')
    date_of_completion = forms.DateField(required=False, label='Date of completion')
    full_description = forms.CharField(max_length=3000, required=False, label='Full description',
                                       widget=widgets.Textarea)
    