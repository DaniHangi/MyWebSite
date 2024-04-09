from django import forms
from base.models import Developer

class DeveloperForm(forms.ModelForm):
  class Meta:
    model = Developer
    fields = ['name', 'biography', 'profile_picture_url', 'email', 'phone_number', 'website_url']

