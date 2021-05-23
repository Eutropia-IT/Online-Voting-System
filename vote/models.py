from django.db import models
from user.models import DummyCitizenInfo, CanInfo

# Create your models here.

class Vote(models.Model):
    elec_name = models.CharField(max_length=40, default='')
    user = models.ForeignKey(DummyCitizenInfo, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(CanInfo, on_delete=models.DO_NOTHING)
    vote_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name + ':' + self.user.nid + '-' + self.candidate.candidate_info.name + '(' + self.candidate.candidate_info.party + ')' 