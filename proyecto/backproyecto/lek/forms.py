from django import forms
from django.contrib.auth.forms import UserCreationForm



# FORMULARIO DE REGISTRO #
class CustomUserCreation(UserCreationForm):
    email = forms.CharField(required=True) #VALIDACION 1
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
