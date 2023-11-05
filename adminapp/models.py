from django.db import models
from datetime import datetime,date,time

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False,unique=True)
    class Meta:
        db_table="admin_table"
    def __str__(self):
        return self.username
class Organisation(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=False,unique=False)
    email=models.CharField(max_length=100,blank=False,unique=True)
    type_choices=(('non-gov','non governmental'),('gov','governmental'))
    type=models.CharField(max_length=100,blank=False,choices=type_choices)
    address=models.TextField(max_length=300,blank=False)
    password=models.CharField(max_length=100,blank=False,unique=True)
    orgaimage=models.FileField(blank=False,upload_to="organisationimage")
    class Meta:
        db_table='organisation_table'
    def __str__(self):
        return self.name
class Donor(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=False,unique=False)
    email=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=50,blank=False,unique=True)
    address=models.TextField(max_length=200,blank=False,unique=False)
    gender_choices=(('male','male'),('female','female'),('others','others'))
    gender=models.CharField(max_length=50,blank=False,choices=gender_choices)
    age=models.IntegerField(blank=False,unique=False)
    class Meta:
        db_table='donor_table'
    def __str__(self):
        return self.name
class Donororgmapping(models.Model):
    mappingid=models.AutoField(primary_key=True)
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE)
    organisation=models.ForeignKey(Organisation,on_delete=models.CASCADE)
    amount=models.IntegerField(unique=False,blank=False,default=0)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    class Meta:
        db_table='donororgmapping_table'
    



