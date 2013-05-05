from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from myCloset.models import UserProfile, ApparelInstance, ApparelType, FriendRequest
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
        fields = ('first_name', 'last_name', 'email', 'gender', 'profilePictureLink')
        
    #adding overridden initialization field, restrict categories to the ones with the user as the author    
    def __init__(self, user, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)      



# form used for adding a new post        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'mainPicture', 'userPictures')
        widgets = {
                   'content' : forms.Textarea,
                   }
        
    #adding overridden initialization field, restrict categories to the ones with the user as the author    
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

## 
#form for adding new apparel instances

class InstanceForm(ModelForm):
    barcode = forms.CharField(max_length = 100)
    class Meta:
        model = ApparelInstance
        fields = ('categories',)
    
    def clean(self):
        cleaned_data = super(InstanceForm, self).clean()
        cleaned_barcode = cleaned_data.get('barcode')
        try:
            ApparelType.objects.get(barcode = cleaned_barcode)              #get or create uncategorized
        except:
            raise forms.ValidationError("The apparel you're trying to add isn't in the database!")
        return cleaned_data
    
##
# Form for creating friend requests

class FriendAddForm(ModelForm):
    class Meta:
        model = FriendRequest
        fields = ('requested_user', 'message')
        
    def __init__(self, this_user, *args, **kwargs):
        super(FriendAddForm, self).__init__(*args, **kwargs)
        self.fields['requested_user'].queryset = UserProfile.objects.exclude(user = this_user)
        
class FriendConfirmForm(ModelForm):
    class Meta:
        model = FriendRequest
        fields = ('response', 'requester')
        
        
        
        
        
        
        
        
        
        
        
        
        
