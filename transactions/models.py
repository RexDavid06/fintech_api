from django.db import models
from wallets.models import Wallet
from uuid import uuid4

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    )
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPE)
    reference = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user} - {self.transaction_type} - {self.amount}"

