from django.urls import path

from api.views import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), 'register'),
]
