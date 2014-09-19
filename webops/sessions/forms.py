from django.forms import ModelForm
from sessions.models import SessionDetails

class SessionForm(ModelForm):
	class Meta:
		model = SessionDetails
		fields = ['author', 'date', 'title', 'description', 'skills']