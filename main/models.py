# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


STATUS = [('Pending', 'Pending'), 
          ('Active', 'Active'),
          ]


class Investments(models.Model):
    uid = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=1000)
    amount = models.CharField(max_length=1000)
    investor = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    roi = models.CharField(max_length=1000)
    status = models.CharField(max_length=7, choices=STATUS)
    unit = models.IntegerField()
    address = models.CharField(max_length=1000)
    fullname = models.CharField(max_length=1000)
    day = models.CharField(max_length=1000, blank=True)
    platform = models.CharField(max_length=1000, blank=True)

   
    

    
    class Meta:
        ordering = ('-plan',)
        verbose_name = 'Investment'
        verbose_name_plural = 'Investments'

    def __str__(self):
        return self.fullname


            
