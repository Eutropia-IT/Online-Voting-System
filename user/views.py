from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserRegistraionForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def dashboard(request):
    pass

def edit_info(request):
    pass

def register(request):
    if request.method == 'POST':
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            pass
        
    form = UserRegistraionForm()
    return render(request, 'home/register.html', {'form' : form})

