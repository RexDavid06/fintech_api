from rest_framework import serializers


class TransferSerializer(serializers.Serializer):
    receiver_id  = serializers.IntegerField()
    amount  =  serializers.DecimalField(max_digits=12, decimal_places=2)
    narration = serializers.CharField(max_length=255, required=False,  allow_blank=True)
    idempotency_key = serializers.CharField()
    