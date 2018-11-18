from django.contrib import admin

# Register your models here.
from bankapp.models import Bank, Branch
from django.contrib import admin

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', )

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'bank', 'city', 'district',
    )
    search_fields = ('name', 'city')
    list_filter = ('bank',)
