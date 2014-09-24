from django.forms import ModelForm
from sessions.models import SessionDetails
from functools import partial
from django import forms

DateInput = partial(forms.DateInput, {'class' : 'datepicker'})

class SessionForm(ModelForm):
	class Meta:
		model = SessionDetails
		fields = ['date', 'title', 'description', 'skills']

class DateForm(forms.Form):
	date = forms.DateField(widget = DateInput())