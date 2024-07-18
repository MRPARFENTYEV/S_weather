import openmeteo_requests
# import requests_cache
# from retry_requests import retry
import statistics
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
#
def get_city_info(city_name):
    # Инициализация геокодера
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
        else:
            return {"error": "Часовой пояс не найден"}
    else:
        return {"error": "Город не найден"}
# print(get_city_info("Moscow"))
#
# # Пример использования функции
# city_name = "Moscow"
# city_info = get_city_info(city_name)
# print(city_info)
# def return_wether(data):
#     cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
#     retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
#     openmeteo = openmeteo_requests.Client(session = retry_session)
#
#     url = "https://api.open-meteo.com/v1/forecast"
#     params = {
#         # "latitude": ret_coord(get_coordinates(place))[0],
#         # "longitude": ret_coord(get_coordinates(place))[1],
#         "latitude": data['latitude'],
#         "longitude": data['longitude'],
#         "hourly": "temperature_2m",
#         "timezone": data['timezone'],
#         "forecast_days": 1
#     }
#     response = requests.get(url,params=params)
#     average_temperature = statistics.mean(response.json()['hourly']['temperature_2m'])
#     return average_temperature
# print(return_wether(get_city_info(city_name)))













# place = 'Moscow'
# country = 'Россия'
# url = "https://nominatim.openstreetmap.org/search.php"
# payload = {
#     "format": "json",
#     "addressdetails": 1,
#     "q": place
# }
# response = requests.get(url, params=payload)
# data = response.json()
# print(data)



# def get_coordinates(city):
#     url = "https://nominatim.openstreetmap.org/search.php"
#     payload = {
#         "format": "json",
#         "addressdetails": 1,
#         "q": city
#     }
#     response = requests.get(url, params=payload)
#     data = response.json()
#     return data
# print(get_coordinates(place))
# #
# def ret_coord(listus):
# 	for info in listus:
# 		return info['lat'], info['lon'], info['name']
# #
# # #____________________________________________________________________________________________
# # #
# cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
# retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
# openmeteo = openmeteo_requests.Client(session = retry_session)
#
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
#     # "latitude": ret_coord(get_coordinates(place))[0],
#     # "longitude": ret_coord(get_coordinates(place))[1],
#     "latitude": 12,
#     "longitude": 25,
#     "hourly": "temperature_2m",
#     "timezone": "Europe/Moscow",
#     "forecast_days": 1
# }
# response = requests.get(url,params=params)
# average_temperature = statistics.mean(response.json()['hourly']['temperature_2m'])
# print(average_temperature)
# import requests
#
# def get_external_ip():
#     response = requests.get('https://api.ipify.org?format=json')
#     external_ip = response.json()['ip']
#     return external_ip
#
# # Пример использования функции
# external_ip = get_external_ip()
# print(f'Внешний IP-адрес: {external_ip}')