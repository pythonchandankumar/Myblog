from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth .forms import AuthenticationForm,UsernameField
from django.utils.translation import  gettext_lazy as _
from .models import Post

class Signup(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm_password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'})}
        

class Login(AuthenticationForm):
        username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
        password=forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current password', 'class':'form-control'}))


class Adam(forms.ModelForm):
     
     class Meta:
          model=Post
          fields=['id','title','content','author','photo']
          labels={'title':'Title','content':'Description','author':'Author'}
          widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                   'content':forms.Textarea(attrs={'class':'form-control'}),
                   'author':forms.TextInput(attrs={'class':'form-control'}),
                   }