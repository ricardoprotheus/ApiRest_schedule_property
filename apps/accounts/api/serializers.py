from rest_framework import serializers

from  accounts.models import User

# esse segue um padrao simples

class  User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'