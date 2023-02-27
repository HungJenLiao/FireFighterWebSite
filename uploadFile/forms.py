from django import forms
from django.forms import ModelForm
from .models import Emergency, Car

class EmergencyForm(ModelForm):
    class Meta:
        model = Emergency
        fields = ('id', 'time', 'car', 'detail', 'location', 'status')
        labels = {
            'time':'YYYY-MM-DD HH:MM:SS',
            'car':'車輛',  
            'detail':'', 
            'location':'', 
            'status':'status(0:待確認, 1:完成)'
        }
        widgets = {
            'time': forms.TextInput(attrs={'class':'form-control', 'placeholder':'time'}),
            'car': forms.TextInput(attrs={'class':'form-control', 'placeholder':'car'}),
            # 'car': forms.Select(attrs={'class':'form-control', 'placeholder':'car'}),
            'detail': forms.TextInput(attrs={'class':'form-control', 'placeholder':'detail'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'location'}), 
            'status': forms.TextInput(attrs={'class':'form-control', 'placeholder':'status'})
        }