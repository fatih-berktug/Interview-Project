from django.db import models
from vira.Model.BaseModel import BaseModel

class CancerType(BaseModel):
    name=models.CharField(max_length=100, null=False, blank=False,
                                    verbose_name='isim')
    def __str__(self):
        return '%s ' % self.name

