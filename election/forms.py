from django.contrib.auth.forms import UserCreationForm, forms
from .models import Election
FRUIT_CHOICES= [ ('national', 'national'),('city', 'city'),]

class createElectionForm(forms.ModelForm):
   

    elec_name = forms.CharField()
    elec_type= forms.CharField(label='ElectionType', widget=forms.Select(choices=FRUIT_CHOICES))
    cvc_file = forms.FileField() 
    class Meta:
        model = Election
        fields = [ 'elec_name',
                   'elec_type',
                   'cvc_file',
            ]
    