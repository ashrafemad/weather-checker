import json

import requests
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.serializers import UserSerializer, UserLoginSerializer, CitySerializer


class CreateUserView(CreateAPIView):
    """
        Create user
        :parameter username [required]
        :parameter email [required]
        :parameter password [required]
    """

    model = User
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer


class LoginView(GenericAPIView):
    """
        User Login
        :parameter username [required]
        :parameter password [required]
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
    """

    http_method_names = ['post']
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid(raise_exception=True):
            response = requests.get(settings.OPEN_WEATHER_MAP_URL,
                                    params={'q': data.validated_data['city_name'],
                                            'appid': settings.OPEN_WEATHER_MAP_KEY})
            json_response = json.loads(response.text)
            if response.status_code == 200:
                weather_details = {'summary': json_response['weather'][0]['main'],
                           'details': json_response['weather'][0]['description']}
                return Response(weather_details,  status=200)
            return Response(data={'error': json_response['message']}, status=json_response['cod'])
        return Response({'error': 'Please enter correct city name'}, status=status.HTTP_400_BAD_REQUEST)
