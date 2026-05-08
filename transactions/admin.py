from django.contrib import admin
from .models import Transaction

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('sender', 'receiver', 'amount', 'idempotency_key', 'status', 'narration', 'timestamp')
    list_display = ['sender', 'receiver', 'amount', 'status']

    def has_add_permission(self, request):
        return False

admin.site.register(Transaction,  TransactionAdmin)
