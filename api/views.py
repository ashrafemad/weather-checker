from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import UserSerializer, UserLoginSerializer


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer


class LoginView(GenericAPIView):
    http_method_names = ['post']
    serializer_class = UserLoginSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            login(user=serialized_data.validated_data, request=request)
            return Response(UserSerializer(request.user).data, status=200)
        return Response(status=status.HTTP_404_NOT_FOUND)
