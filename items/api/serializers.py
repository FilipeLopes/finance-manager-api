from rest_framework.serializers import ModelSerializer
from items.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'user', 'name', 'value', 'date', 'categories')
