from django import forms 
from .models import Register

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name',
                   'phone_number', 'email', 'password', 'DOB']
        
        widgets = {
            'DOB': forms.DateTimeInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput()
        }
        