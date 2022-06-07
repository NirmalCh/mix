from rest_framework import serializers
from .models import Account_info

class Account_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_info
        # fields = ['id', 'account_number', 'citizenship_no', 'user']
        fields = '__all__'