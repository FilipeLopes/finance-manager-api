from rest_framework.viewsets import ModelViewSet
from items.models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
