import pandas as pd
from user import forms
from user.models import CanInfo, DummyCitizenInfo
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Election
from user.models import DummyCitizenInfo,CanInfo
from vote.models import Vote
from .forms import *
from django.db.models import Q

# Create your views here.
@login_required
def election(request, elecName):
    votearea = DummyCitizenInfo.objects.get(email = request.user.email)
    electionobj = Election.objects.get(elec_name=elecName)
    admincandidates = CanInfo.objects.filter(elec_name = elecName)
    if(electionobj.elec_type=='national'):
        candidates=CanInfo.objects.filter(elec_name = elecName, voting_area = votearea.area_name)
    else:
        # mayorcandidates=CanInfo.objects.filter(elec_name = elecName, candidate_type = 'MAYOR') 
        candidates=CanInfo.objects.filter(Q(elec_name = elecName) & Q(voting_ward = votearea.ward_number)|Q(voting_ward = 'M'))
    print(admincandidates)
        
    canlistname = []
    canlistphoto = []
    candiparty = []
    canlisttype = []
    canlistnid = []
    counter = []
    canlistward =[]
    canlistarea = []
    
    admincanlistname = []
    admincanlistphoto = []
    admincandiparty = []
    admincanlisttype = []
    admincanlistnid = []
    admincounter = []
    admincanlistward =[]
    admincanlistarea = []
    for j in range(len(admincandidates)):
        dummyvar=DummyCitizenInfo.objects.get(nid = admincandidates[j].nid)
        admincanlistname.append(dummyvar.name)
        admincanlistphoto.append(dummyvar.picture)
        admincanlisttype.append(admincandidates[j].candidate_type)
        admincandiparty.append(admincandidates[j].party_name)
        admincanlistnid.append(admincandidates[j].nid)
        admincanlistward.append(admincandidates[j].voting_ward)
        admincanlistarea.append(admincandidates[j].voting_area)
        admincounter.append(Vote.objects.filter(elec_name=elecName,candidate=admincandidates[j]).count())
    
    for i in range(len(candidates)):
        dummyvar=DummyCitizenInfo.objects.get(nid = candidates[i].nid)
        canlistname.append(dummyvar.name)
        canlistphoto.append(dummyvar.picture)
        canlisttype.append(candidates[i].candidate_type)
        candiparty.append(candidates[i].party_name)
        canlistnid.append(candidates[i].nid)
        canlistward.append(candidates[i].voting_ward)
        canlistarea.append(candidates[i].voting_area)
        counter.append(Vote.objects.filter(elec_name=elecName,candidate=candidates[i]).count())
    print(canlistname)
    flag = Vote.objects.filter(elec_name=elecName, user=DummyCitizenInfo.objects.get(email=request.user.email), vote_status= True)
    context = {
        'uData' : DummyCitizenInfo.objects.get(email = request.user.email),
        'getElectionData': CanInfo.objects.filter(elec_name = elecName),
        'electionTable' : Election.objects.get(elec_name = elecName),
        'elec_name' : elecName,
        'admincanlistcity' : zip(admincanlistname,admincanlisttype,admincanlistward,admincounter),
        'admincanlistnational' : zip(admincanlistname,admincandiparty,admincanlistarea,admincounter),
        'canlist' :  zip(canlistname,canlistphoto,canlisttype,candiparty,canlistnid),
        'canlist1' :  zip(canlistname,canlistphoto,canlisttype,candiparty,canlistnid),
        'canlist2' :  zip(canlistname,canlistphoto,canlisttype,candiparty,canlistnid),
        'canlist3' :  zip(canlistname,canlisttype,canlistward,counter),
        'nationalcanlist' :  zip(canlistname,candiparty,canlistarea,counter),
        'voteFlag' : flag,
        'votearea' : votearea
    }
    if request.method == 'POST':
        et = Election.objects.get(elec_name = elecName)
        if request.POST.get('actionOp') == 'active':
            et.elec_status = request.POST.get('actionOp')
            et.save()
        if request.POST.get('actionOp') == 'cancle':
            Election.objects.get(elec_name = elecName).delete()
            CanInfo.objects.filter(elec_name = elecName).delete()
        if request.POST.get('actionOp') == 'ended':
            et.elec_status = 'ended'
            et.save()
        if request.POST.get('MAYOR') and request.POST.get('COUNCILLOR') and request.POST.get('RESERVED'):
            vModel1 = Vote(elec_name=elecName, vote_status= True, user=DummyCitizenInfo.objects.get(email=request.user.email), candidate = CanInfo.objects.filter(candidate_type='MAYOR').get(nid=request.POST.get('MAYOR')))
            vModel2 = Vote(elec_name=elecName, vote_status= True, user=DummyCitizenInfo.objects.get(email=request.user.email), candidate = CanInfo.objects.filter(candidate_type='COUNCILLOR').get(nid=request.POST.get('COUNCILLOR')))
            vModel3 = Vote(elec_name=elecName, vote_status= True, user=DummyCitizenInfo.objects.get(email=request.user.email), candidate = CanInfo.objects.filter(candidate_type='RESERVED').get(nid=request.POST.get('RESERVED')))
            vModel1.save()
            vModel2.save()
            vModel3.save()
        if request.POST.get('MP'):
            vModel1 = Vote(elec_name=elecName, vote_status= True, user=DummyCitizenInfo.objects.get(email=request.user.email), candidate = CanInfo.objects.filter(candidate_type='MP',elec_name=elecName).get(nid=request.POST.get('MP')))
            vModel1.save()
            
        checkAccess = DummyCitizenInfo.objects.get(email=request.user.email)
        if checkAccess.elec_Worker == True:
            return redirect('election-worker')
        else:
            return redirect('dashboard')
    elif Election.objects.filter(elec_name = elecName, elec_type = 'national'):
        return render(request, 'home/national.html', context)
    elif Election.objects.filter(elec_name = elecName, elec_type = 'city'):
        return render(request, 'home/city.html', context)

@login_required
def electionWorker(request):
    context = {
        "pElectionList" : Election.objects.filter(elec_status='pending'),
        "aElectionList" : Election.objects.filter(elec_status='active'),
        "userInfo" : DummyCitizenInfo.objects.get(email=request.user.email),
        "clec_createForm" : createElectionForm(),
    }
    if request.method == 'POST':  
        if len(request.FILES) !=0:
            df = pd.read_csv(request.FILES['cvc_file'])
            
            if request.POST.get('elec_type') == 'national':
                for i in range(len(df)):
                    can = CanInfo(
                        name= df['name'][i],
                        nid = df['nid'][i],
                        elec_name=request.POST.get('elec_name'),
                        candidate_type=df['candidate_type'][i],
                        party_name = df['party_name'][i],
                        voting_area = df['Area Name'][i],
                    )
                    can.save()
                elect = Election(
                        elec_name = request.POST.get('elec_name'),
                        elec_type = request.POST.get('elec_type')
                    )
                elect.save()
                    
            else:
                for i in range(len(df)):
                    can = CanInfo(
                        name= df['name'][i],
                        nid = df['nid'][i],
                        elec_name=request.POST.get('elec_name'),
                        candidate_type=df['candidate_type'][i],
                        voting_ward = df['Ward Number'][i],
                    )
                    can.save()
                elect = Election(
                        elec_name = request.POST.get('elec_name'),
                        elec_type = request.POST.get('elec_type')
                    )
                elect.save()
            
            return redirect('election-worker')
    return render(request, 'home/elec-worker.html', context)

def aricves(request):
    context = {
        'eAcrives' : Election.objects.filter(elec_status= 'ended')
    }
    return render(request, 'home/arcives.html', context)

def publicResult(request, elecName):
    
    electionobj = Election.objects.get(elec_name=elecName)
    
    
    candidates=CanInfo.objects.filter(elec_name = elecName)


    canlistname = []
    canlistphoto = []
    candiparty = []
    canlisttype = []
    canlistnid = []
    counter = []
    canlistward =[]
    canlistarea = []
    
    for i in range(len(candidates)):
        dummyvar=DummyCitizenInfo.objects.get(nid = candidates[i].nid)
        canlistname.append(dummyvar.name)
        canlistphoto.append(dummyvar.picture)
        canlisttype.append(candidates[i].candidate_type)
        candiparty.append(candidates[i].party_name)
        canlistnid.append(candidates[i].nid)
        canlistward.append(candidates[i].voting_ward)
        canlistarea.append(candidates[i].voting_area)
        counter.append(Vote.objects.filter(elec_name=elecName,candidate=candidates[i]).count())

    #flag = Vote.objects.filter(elec_name=elecName, user=DummyCitizenInfo.objects.get(email=request.user.email), vote_status= True)
    context = {
        #'uData' : DummyCitizenInfo.objects.get(email = request.user.email),
        'getElectionData': CanInfo.objects.filter(elec_name = elecName),
        'electionTable' : Election.objects.get(elec_name = elecName),
        'elec_name' : elecName,
        'canlist' :  zip(canlistname,canlistphoto,canlisttype,candiparty,canlistnid),
        'canlist1' :  zip(canlistname,canlistphoto,canlisttype,candiparty,canlistnid),
        'canlist2' :  zip(canlistname,canlistphoto,canlisttype,candiparty,canlistnid),
        'canlist3' :  zip(canlistname,canlisttype,canlistward,counter),
        'nationalcanlist' :  zip(canlistname,candiparty,canlistarea,counter),
        
    }
    if Election.objects.filter(elec_name = elecName, elec_type = 'national'):
        context['nTable'] = True
    
    return render(request, 'home/arciverus.html', context)