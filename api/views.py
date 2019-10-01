from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.serializers import UserSerializer, UserLoginSerializer, CitySerializer
from api.utils import get_weather_data


class CreateUserView(CreateAPIView):
    """
        Create user
        :parameter username [required]
        :parameter email [required]
        :parameter password [required]
        :returns user data (email, username)
    """

    model = User
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer


class LoginView(GenericAPIView):
    """
        User Login
        :parameter username [required]
        :parameter password [required]
        :returns user data (email, username)
    """

    http_method_names = ['post']
    serializer_class = UserLoginSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            login(user=serialized_data.validated_data, request=request)
            return Response(UserSerializer(request.user).data, status=200)
        return Response(status=status.HTTP_404_NOT_FOUND)


class WeatherDetailsView(GenericAPIView):
    """
        Weather information
        :parameter city_name [required]
        :returns on success {summary: one word describing weather state, details: more detailed info about weather}
    """

    http_method_names = ['post']
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid(raise_exception=True):
            response = get_weather_data(city_name=data.validated_data['city_name'])
            if response.get('details', None) and response.get('status') == 200:
                return Response(response['details'], status=200)
            return Response(data={'error': response['error']}, status=response['status'])
        return Response({'error': 'Please enter correct city name'}, status=status.HTTP_400_BAD_REQUEST)
