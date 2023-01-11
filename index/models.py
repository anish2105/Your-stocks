from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.contrib.auth.models import User
# User = settings.AUTH_USER_MODEL
# Create your models here.
class stocks(models.Model):
    id = models.AutoField(primary_key=True)
    nameofstocks = models.CharField(max_length= 30)
    buy = models.DecimalField( max_digits = 8,default=0,null=True, blank=True, decimal_places=2)
    buydate = models.DateTimeField(default=now,null=True, blank=True)
    sell = models.DecimalField( max_digits = 8,default=0,null=True, blank=True, decimal_places=2)
    selldate = models.DateTimeField(default=now,null=True, blank=True)
    t1 = models.DecimalField( max_digits = 8,default=0, null=True, blank=True, decimal_places=2)
    t2 = models.DecimalField( max_digits = 8,default=0, null=True, blank=True, decimal_places=2)
    user = models.ForeignKey(User,default = None,on_delete=models.CASCADE)

    def __str__(self):
        return self.nameofstocks

    

    def calculate(self):
        if(self.buy != None or self.sell != None):
            profit =  self.sell - self.buy
            # t_p.append(profit)
            return profit

        else:
            return None
