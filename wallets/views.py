from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.permissions import IsAuthenticated
from  .models import Wallet
from rest_framework.response import Response
from  rest_framework.status import HTTP_200_OK

# Create your views here.
class WalletView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,  request):
        wallet = Wallet.objects.get(user=request.user)
        return Response({
            'wallet_balance': wallet.balance,
        }, status=HTTP_200_OK)
        
    