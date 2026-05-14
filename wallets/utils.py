import random
from  .models import Wallet

def generate_account_number():
    while True:
        account_number = str(random.randint(1000000000, 9999999999))
        if not Wallet.objects.filter(account_number=account_number).exists():
            return account_number
            