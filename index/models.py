from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.contrib.auth.models import User
# User = settings.AUTH_USER_MODEL
# Create your models here.
class stocks(models.Model):
    id = models.AutoField(primary_key=True)
    nameofstocks = models.CharField(max_length= 30)
    buy = models.IntegerField(default=0,null=True, blank=True)
    buydate = models.DateTimeField(default=now,null=True, blank=True)
    sell = models.IntegerField(default=0,null=True, blank=True)
    selldate = models.DateTimeField(default=now,null=True, blank=True)
    t1 = models.IntegerField(default=0, null=True, blank=True)
    t2 = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User,default = None,on_delete=models.CASCADE)

    def __str__(self):
        return self.nameofstocks
