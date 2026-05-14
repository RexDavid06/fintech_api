from django.contrib import admin
from .models import Wallet

# Register your models here.
class WalletAdmin(admin.ModelAdmin):
    list_display  = ['user', 'balance', 'account_number']
    readonly_fields = ['user',   'balance',  'account_number']

    def has_add_permission(self,   request):
        return False

admin.site.register(Wallet,   WalletAdmin)