from django import forms 
# Registeration Module
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required



@login_required                                                                                                       
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #CHOICE = [('UNIT 1', 'UNIT 1'), ('UNIT 2', 'UNIT 2'), ('UNIT 3', 'UNIT 3')]
    #unit = forms.CharField(max_length=10, Choices=CHOICE)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']



@login_required
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email'] 


@login_required
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'location', 'image']
