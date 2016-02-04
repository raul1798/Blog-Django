from django import forms
from .models import CustomUser
from django.forms import Textarea
from django.forms.extras.widgets import SelectDateWidget



class ProfileForm(forms.ModelForm):
	
	class Meta:
		model = CustomUser
		fields = ('avatar', 'firstname', 'lastname',
				'date_of_birth','about_user', 'username')

		widgets = {
			'date_of_birth': SelectDateWidget(years=range(1920, 2015)),
			'about_user' : Textarea(attrs={'cols':80, 'rows':5})
			}