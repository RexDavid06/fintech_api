from rest_framework import serializer 
from .models import Transaction


class TransactionSerializer(serializer.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'reference', 'created_at']
        
