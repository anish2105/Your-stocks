from django.db import models

# Create your models here.
class stocks(models.Model):
    id = models.AutoField(primary_key=True)
    nameofstocks = models.CharField(max_length= 30)
    buy = models.IntegerField()
    buydate = models.DateField(null=True, blank=True)
    sell = models.IntegerField()
    selldate = models.DateField(null=True, blank=True)
    t1 = models.IntegerField( null=True, blank=True)
    t2 = models.IntegerField( null=True, blank=True)
    profit  = models.BooleanField(null=True, blank=True)
    loss = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.nameofstocks
