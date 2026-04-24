from django.db import models
from  django.conf import settings

User= settings.AUTH_USER_MODEL

# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2,  default='0.0')

    def __str__(self):
        return f"{self.user} Wallet!"

