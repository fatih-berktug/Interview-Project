from django.db import models
from vira.Model.BaseModel import BaseModel
from vira.Model.CancerType import CancerType

class Patient(BaseModel):
    name=models.CharField(max_length=100, null=False, blank=False,
                                    verbose_name='isim')
    surname=models.CharField(max_length=100, null=False, blank=False,
                                    verbose_name='soyisim')
    tc=models.CharField(max_length=100, null=False, blank=False,
                                    verbose_name='tc')
    cancerType=models.ForeignKey(CancerType,on_delete=models.CASCADE)



