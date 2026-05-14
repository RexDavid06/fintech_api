from rest_framework import serializers
from .models import Wallet


class TransferSerializer(serializers.Serializer):
    account_number  = serializers.IntegerField()
    amount  =  serializers.DecimalField(max_digits=12, decimal_places=2)
    narration = serializers.CharField(max_length=255, required=False,  allow_blank=True)
    idempotency_key = serializers.CharField()


    def validate_account_number(self,  value):
        if not Wallet.objects.filter(account_number=value).exists():
            raise serializers.ValidationError('Invalid account number')
        return value
