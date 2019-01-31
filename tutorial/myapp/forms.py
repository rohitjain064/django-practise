from django import forms
from.models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

class Student_form(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter name"}),required=True,max_length=100)
    email_id=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter email id"}),required=True)
    city=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter city"}),required=True,max_length=21)
    marks=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter marks"}),required=True,max_length=10)

    class Meta():
        model=Student
        fields=['name','email_id','city','marks']


class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username"}),required=True,max_length=50)
    email=forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder":"Enter email"}),required=True,max_length=50)
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter first name"}),required=True,max_length=50)
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your last name"}),required=True,max_length=50)
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter password"}),required=True,max_length=50)
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Conirm password"}),required=True,max_length=50)

    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']


    def clean_username(self):
        user=self.cleaned_data['username']
        try:
            match=User.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("username alerady exit")
    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            match=User.objects.get(email=email)
            match=mt=validate_email(email)
        except:
            return forms.ValidationError("Email is not in correct format")
        return email
    def clean_confirm_password(self):
        pas=self.cleaned_data['password']
        cpas=self.cleaned_data['confirm_password']
        MIN_LENGTH=8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError("password and confirm  password not matchrd")
            else:
                if len(pas)<MIN_LENGTH:
                    raise forms.ValidationError("password should have atleast %d characters" %MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError('password should not all numeric')

