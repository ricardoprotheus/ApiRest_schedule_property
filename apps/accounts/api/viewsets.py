from rest_framework import viewsets

from  accounts.models import User
from  accounts.api.serializers import User_serializer


class User_viewsets(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = User_serializer