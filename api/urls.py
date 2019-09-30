from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from api.views import CreateUserView, LoginView, WeatherDetailsView

schema_view = get_swagger_view(title='Weather Checker API')

urlpatterns = [
    path('docs/', schema_view),
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('weather/', WeatherDetailsView.as_view(), name='login'),
]
