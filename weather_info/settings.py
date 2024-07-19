from django.urls import path
from . import views
app_name = 'weather_info'

urlpatterns = [
    path('', views.show_weather_to_user, name='show_weather_to_user'),]
