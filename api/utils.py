import json
import requests
from django.conf import settings


def get_weather_data(city_name):
    response = requests.get(settings.OPEN_WEATHER_MAP_URL,
                            params={'q':city_name,
                                    'appid': settings.OPEN_WEATHER_MAP_KEY})
    json_response = json.loads(response.text)
    if response.status_code == 200:
        weather_details = {'summary': json_response['weather'][0]['main'],
                           'details': json_response['weather'][0]['description']}
        return {'details': weather_details, 'status': 200}
    return {'error': json_response['message'], 'status': json_response['cod']}