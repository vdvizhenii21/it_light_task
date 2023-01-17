from rest_framework import mixins, viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
