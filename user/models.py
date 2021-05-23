from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DummyCitizenInfo(models.Model):
    picture = models.FileField(upload_to='profile_pictures', default='default.jpg')
    name = models.CharField(max_length=30, db_column='Name')
    father_name = models.CharField(max_length=30, db_column='Father Name')
    mother_name = models.CharField(max_length=30, db_column='Mother Name')
    nid = models.CharField(max_length=16,default='')
    gender = models.CharField(max_length=6,default='',blank=True)
    email = models.EmailField(max_length=19 , db_column='Email')
    phone = models.CharField(max_length=11 , db_column='Phone Number')
    area_name = models.CharField(max_length=10, db_column='Area Name')
    ward_number = models.CharField(max_length=10, db_column='Ward Number')
    dob = models.DateField()
    elec_Worker = models.BooleanField(default=False)

    def __str__(self):
        return self.name+ '-' + self.nid

class CanInfo(models.Model):
    name =  models.CharField(max_length=40, default='')
    nid = models.CharField(max_length=40, default='')
    elec_name = models.CharField(max_length=41, default='')  
    mp = 'MP'
    mayor = 'MAYOR'
    councillor = 'COUNCILLOR'
    resereved_lady = 'RESERVED'
    options1 = [
        (mp, 'MP'),
        (mayor, 'MAYOR'),
        (councillor, 'COUNCILLOR'),
        (resereved_lady, 'RESERVED')
    ]
    candidate_type = models.TextField(choices=options1)
    al = 'AL'
    bnp = 'BNP'
    jp = 'JP'
    communist = 'COMMUNIST'
    self_party = 'SELF PARTY'
    options2 = [
        (al, 'AL'),
        (bnp, 'BNP'),
        (jp, 'JP'),
        (communist, 'COMMUNIST'),
        (self_party, 'SELF PARTY'),
    ]
    party_name = models.TextField(choices=options2)
    voting_area = models.CharField(default='', max_length=10, db_column='Area Name')
    voting_ward = models.CharField(default='' , max_length=10 ,db_column='Ward Number')

    def __str__(self):
        return self.name+ '-' + self.voting_area + '-' + self.voting_ward

