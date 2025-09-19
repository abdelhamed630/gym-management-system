from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput,PasswordInput
from .models import record


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    
    
class CreateRecord(forms.ModelForm):
    class  Meta:
      model=record
      fields="__all__"
      
      
class UpdateRecordForm(forms.ModelForm):
    class  Meta:
        model=record
        fields="__all__"
        
   
