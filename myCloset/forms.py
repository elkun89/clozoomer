from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from myCloset.models import UserProfile
from django.db.models import Q
from myCloset.models import Post

class UserForm(forms.Form):
    
    username = forms.CharField(max_length = 50)
    first_name = forms.CharField(label="First Name",max_length = 20)
    last_name = forms.CharField(label="Last Name", max_length = 20)
    email = forms.EmailField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices = GENDER, widget = forms.RadioSelect())
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
    
class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'gender','friends', 'profilePictureLink')
        
    #adding overridden initialization field, restrict categories to the ones with the user as the author    
    def __init__(self, user, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)      



# form used for adding a new post        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'mainPicture', 'userPictures')
        
    #adding overridden initialization field, restrict categories to the ones with the user as the author    
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        
    #content = forms.CharField(max_length = 500)
    #mainPicture = forms.ImageField(upload_to = 'users', blank = True)
    #userPictures = forms.ImageField(upload_to = 'users' blank = True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
