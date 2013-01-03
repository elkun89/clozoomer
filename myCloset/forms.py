from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.db.models import Q

class UserForm(forms.Form):
    username = forms.CharField(max_length = 50)
    first_name = forms.CharField(label="First Name",max_length = 20)
    last_name = forms.CharField(label="Last Name", max_length = 20)
    email = forms.EmailField()
    newPassword = forms.CharField(label="Password", widget=forms.PasswordInput)
    newPasswordConfirm = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput,
                                help_text = "Enter the same password as above, for verification.")
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        usernameData = cleaned_data.get('username')
        newPassword = cleaned_data.get('newPassword')
        newPasswordConfirm = cleaned_data.get('newPasswordConfirm')
        if(User.objects.filter(username = usernameData).count() >= 1):
            raise forms.ValidationError("A user with that username already exists, and I will not let you make another one.")
        elif not newPassword == newPasswordConfirm:
            raise forms.ValidationError("You have unmatching passwords!")
        
        return cleaned_data