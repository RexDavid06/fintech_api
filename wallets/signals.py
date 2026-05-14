from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import Wallet
from .utils import generate_account_number

User=settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(
            user=instance,
            account_number=generate_account_number()
            )