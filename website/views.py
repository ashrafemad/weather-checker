from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from api.utils import get_weather_data


class UserLoginView(LoginView):
    template_name = 'website/login.html'
    extra_context = {'title': 'Weather Checker - Login'}


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


@method_decorator(login_required, name='dispatch')
class WeatherDetails(View):
    def get(self, request):
        return render(request, 'website/weather.html', context={'title': 'Weather Info'})

    def post(self, request):
        city_name = request.POST.get('city_name', None)
        if city_name:
            response = get_weather_data(city_name=city_name)
            if response.get('details', None) and response.get('status') == 200:
                context = {'title': f'{city_name}: Weather Details', 'details': response['details']}
            else:
                context = {'title': f'{city_name}: Weather Details', 'error': response['error']}
            return render(request, 'website/weather.html', context=context)
        context = {'title': 'Weather Info', 'error': 'No City Entered'}
        return render(request, 'website/weather.html', context=context)