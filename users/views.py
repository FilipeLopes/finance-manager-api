from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from users.api.serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
# Class based view to Get User Details using Token Authentication


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)

        serializer = UserSerializer(user)
        return Response(serializer.data)

# Class based view to register user


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserLogInAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        print(token)
        return Response({
            'token': token[0].key,
            'id': user.pk,
            'username': user.username
        })


class UserLogoutAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token.delete()

        return Response({'detail': 'Logged out successfully'})
