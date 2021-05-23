from django.contrib.admin import options
from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Election(models.Model):
    elec_name = CharField(max_length=40, default=' ')

    national = "national"
    city ='city'
    opt = [(national, "national"), (city,'city')]
    elec_type = TextField(choices=opt)
    
    active = 'active'
    panding = 'pending'
    cancel = 'cancle'
    ended = 'ended'
    opt2 = [ ( active, 'active') , (panding , 'pending'), (cancel ,'cancle'), (ended ,'ended')]
    elec_status = TextField(choices=opt2, default='pending')
