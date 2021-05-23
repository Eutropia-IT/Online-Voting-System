import pandas as pd
from user import forms
from user.models import CandidateInfo, DummyCitizenInfo
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Election
from user.models import DummyCitizenInfo,CandidateInfo
from .forms import *

# Create your views here.
@login_required
def election(request, elecName):
    context = {
        'uData' : DummyCitizenInfo.objects.get(email = request.user.email),
        'getElectionData': CandidateInfo.objects.filter(elec_name = elecName)
    }
    print(CandidateInfo.objects.filter(elec_name = str(elecName)))
    if Election.objects.filter(elec_name = elecName, elec_type = 'national'):
        return render(request, 'home/national.html', context)
    elif Election.objects.filter(elec_name = elecName, elec_type = 'city'):
        return render(request, 'home/city.html', context)

@login_required
def electionWorker(request):
    context = {
        "electionList" : Election.objects.all(),
        "userInfo" : DummyCitizenInfo.objects.get(email=request.user.email),
        "clec_createForm" : createElectionForm(),
    }
    if request.method == 'POST':  
        if len(request.FILES) !=0:
            df = pd.read_csv(request.FILES['cvc_file'])
            elect = Election(
                            elec_name = request.POST.get('elec_name'),
                            elec_type = request.POST.get('elec_type')
                        )
            elect.save()
            if request.POST.get('elec_type') == 'national':
                for i in range(len(df)):
                    can = CandidateInfo(
                        nid= df['nid'][i],
                        elec_name=request.POST.get('elec_name'),
                        candidate_type=df['candidatetype'][i],
                        party_name = df['partyname'][i],
                        voting_area = df['area'][i],
                    )
                    can.save()
            else:
                for i in range(len(df)):
                    can = CandidateInfo(
                        nid= df['nid'][i],
                        elec_name=request.POST.get('elec_name'),
                        candidate_type=df['candidatetype'][i],
                        voting_ward = df['ward'][i],
                    )
                    can.save()
            return redirect('election-worker ')
    return render(request, 'home/elec-worker.html', context)