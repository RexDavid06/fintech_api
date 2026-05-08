from django.db import models
from wallets.models import Wallet
from uuid import uuid4
from django.conf import settings

# Create your models here.
class Transaction(models.Model):
    STATUS = (
        ("PENDING", "Pending"),
        ("FAILED", "Failed"),
        ("SUCCESS", "Success"),
    )

    id = models.UUIDField(default=uuid4, primary_key=True,  editable=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='sent_tnx')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='received_tnx')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    idempotency_key = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=7, choices=STATUS)
    narration = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

