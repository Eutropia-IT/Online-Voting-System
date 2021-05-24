from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from election.models import Election
from .models import CanInfo, DummyCitizenInfo
from django.conf import settings

# Create your views here.
@login_required
def dashboard(request):
    context = {
        "aElectionList" : Election.objects.filter(elec_status = 'active'),
        "endElectionList" : Election.objects.filter(elec_status = 'ended'),
        "userInfo" : DummyCitizenInfo.objects.get(email=request.user.email)
    }
    if context['userInfo'].elec_Worker == True:
        return redirect('election-worker')
    else:
        return render(request, 'home/dashboard.html', context)

@login_required
def edit_info(request):
    context = {
        'editInfoForm' : EditInfoForm(),
        "userInfo" : DummyCitizenInfo.objects.get(email=request.user.email)
    }
    if request.method == "POST":
        uemail=request.user.email
        var = DummyCitizenInfo.objects.get(email=uemail)
        edit_profile_form = EditInfoForm(request.POST, request.FILES, instance=var)
        if edit_profile_form.is_valid():
            if len(request.FILES) !=0:
                context['userInfo'].picture = request.FILES['profile_picture']
                context['userInfo'].save()
            if  request.POST.get('name') and request.POST.get('father_name') and request.POST.get('mother_name') and request.POST.get('dob'):
                context['userInfo'].name = request.POST.get('name')
                context['userInfo'].father_name = request.POST.get('father_name')
                context['userInfo'].mother_name = request.POST.get('mother_name')
                context['userInfo'].dob = request.POST.get('dob')
                context['userInfo'].save()
            return redirect('dashboard')
        
    return render(request, 'home/editProfile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            user_nid = request.POST.get('nid')
            try:
                var_nid = DummyCitizenInfo.objects.get(nid = user_nid)
                
                if var_nid:
                    form.save()
                    new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
                    login(request, new_user)
                    return redirect('dashboard')
            except ObjectDoesNotExist:
                
                return redirect('login')
                
    else:
        form = UserRegistraionForm()
    return render(request, 'home/register.html', {'form' : form})

