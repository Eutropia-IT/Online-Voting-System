from user.models import DummyCitizenInfo
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User, models




class UserRegistraionForm(UserCreationForm):
    email = forms.EmailField()
    nid = forms.CharField()
    phone = forms.CharField()
    class Meta:
        model = User
        nid = models.CharField(unique=True)
        fields = [ 'username',
                   'email',
                   'nid',
                   'phone',
                   'password1',
                   'password2',
            ]

class EditInfoForm(forms.ModelForm):
    name = forms.CharField()
    father_name = forms.CharField()
    mother_name = forms.CharField()
    profile_picture = forms.FileField()
    dob = forms.DateField()
    class Meta:
        model = DummyCitizenInfo
        fields = [
            'name',
            'father_name',
            'mother_name',
            'profile_picture',
            'dob'
        ]






