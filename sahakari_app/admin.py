from django.contrib import admin
from . models import Account_info, City
# Register your models here.
# admin.site.register(models.Account_info)

class Account_InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','account_number')
  
admin.site.register(Account_info, Account_InfoAdmin)
admin.site.register(City)