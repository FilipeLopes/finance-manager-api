from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
