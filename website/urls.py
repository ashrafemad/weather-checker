from django.urls import path

from website.views import UserLoginView, LogoutView, WeatherDetails

urlpatterns = [
    path('', WeatherDetails.as_view(), name='weather-details'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
