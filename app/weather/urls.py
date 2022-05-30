from django.urls import path
from weather import views as api_views

urlpatterns = [
   path('weatherforecast', api_views.WeatherForecastView.as_view(), name='weather-forecast'),
   path('province', api_views.ProvinceVeiw.as_view(), name='province-list' ),
   path('weather', api_views.WeatherView.as_view(), name='weather'),
   path('town', api_views.TownView.as_view(), name='town'),
   path('weather/<int:pk>', api_views.WeatherDetailWeather.as_view(), name='town-update'),
   path('province/<int:pk>', api_views.ProvinceDetailWeather.as_view(), name='town-add'),
   path('town/<int:pk>', api_views.TownDetailWeather.as_view(), name='town-add')
]