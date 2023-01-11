from django.db import models

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length=254)
    phone = models.DecimalField(max_digits = 10,decimal_places=0)
    desc = models.CharField(max_length = 75)
