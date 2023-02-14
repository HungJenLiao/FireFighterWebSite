from django import forms
from django.forms import ModelForm
from .models import Emergency

class EmergencyForm(ModelForm):
    class Meta:
        model = Emergency
        fields = ('id', 'time', 'car', 'detail', 'location', 'status')
        labels = {
            'time':'',
            'car':'',  
            'detail':'', 
            'location':'', 
            'status':''
        }
        widgets = {
            'time': forms.DateTimeInput(attrs={'class':'form-control', 'type': 'datetime-local'}),
            'car': forms.TextInput(attrs={'class':'form-control', 'placeholder':'car'}),
            'detail': forms.TextInput(attrs={'class':'form-control', 'placeholder':'detail'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'location'}), 
            'status': forms.TextInput(attrs={'class':'form-control', 'placeholder':'status'})
        }