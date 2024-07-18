from django.shortcuts import render
# from weather_info.models import  User, UserQuery
import openmeteo_requests
import requests_cache
from retry_requests import retry
import statistics
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
from forms import InputCityForm
def get_city_info(city_name): # выводит город, широту, долготу, временную зону

    geolocator = Nominatim(user_agent="city_info")
    location = geolocator.geocode(city_name)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=longitude, lat=latitude)

        if timezone_str:
            timezone = pytz.timezone(timezone_str)
            local_time = datetime.now(timezone)

            return {
                "city": city_name,
                "latitude": latitude,
                "longitude": longitude,
                "timezone": timezone_str,
                "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S')
            }



def get_external_ip(): # Вычислить ip
    response = requests.get('https://api.ipify.org?format=json')
    external_ip = response.json()['ip']
    return external_ip


def return_wether(data):
    form = InputCityForm(request.POST)# измена
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        # "latitude": ret_coord(get_coordinates(place))[0],
        # "longitude": ret_coord(get_coordinates(place))[1],
        "latitude": data['latitude'],
        "longitude": data['longitude'],
        "hourly": "temperature_2m",
        "timezone": data['timezone'],
        "forecast_days": 1
    }
    response = requests.get(url,params=params)
    temp = response.json()['hourly']['temperature_2m']
    average_temperature = statistics.mean(response.json()['hourly']['temperature_2m'])
    return int(average_temperature)
print(return_wether(get_city_info('Moscow')))
