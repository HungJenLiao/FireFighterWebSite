from django import forms
from django.forms import ModelForm
from .models import Emergency

class EmergencyForm(ModelForm):
    class Meta:
        model = Emergency
        fields = "__all__"