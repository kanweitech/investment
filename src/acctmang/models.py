from django.db import models

# Create your models here.
class User(models.Model):
    """
    This Enitre Django system is esssentially a decoupled system. This User Model in this case
    isn't managed by Django. This record is inspected reqularly for better ORM query
    """
    class Meta:
        managed = False
        db_table = 'users'
        
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    regdate = models.CharField(max_length=1000)
    birth = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    bank = models.CharField(max_length=1000)
    accnumber = models.CharField(max_length=1000)
    refcode = models.CharField(max_length=1000)
    sponsor = models.CharField(max_length=1000)
    refactive = models.CharField(max_length=1000)
    refwallet = models.CharField(max_length=1000)
    blaze_wallet = models.CharField(max_length=1000)
    bbb_plan = models.CharField(max_length=1000)
    kin_name = models.CharField(max_length=1000)
    kin_email = models.CharField(max_length=1000)
    kin_phone = models.CharField(max_length=1000)
    kin_rel = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return str(self.name)