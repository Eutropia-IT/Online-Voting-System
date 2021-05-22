from django.db import models
from user.models import DummyCitizenInfo, CandidateInfo

# Create your models here.

class Vote(models.Model):
    user = models.OneToOneField(DummyCitizenInfo, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(CandidateInfo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.name + ':' + self.user.nid + '-' + self.candidate.candidate_info.name + '(' + self.candidate.candidate_info.party + ')' 