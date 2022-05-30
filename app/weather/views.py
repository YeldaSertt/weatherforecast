from rest_framework.views import APIView
from weather.serializers import *
from weather.models import Province, Town, Weather
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_data_from_cache(key):
    path = settings.CACHE_KEY_PATH.format(key)
    return cache.get(path), path

class WeatherForecastView(APIView):
    """
    weather information and filtering of all provinces and districts
    """
    def get(self, request):
        data, path = get_data_from_cache("weatherforecast")
        if not data:
            province_filter = request.query_params.get("province")
            province = Province.objects.prefetch_related("province_weather").filter(deleted=0)
            if province_filter:
                province = province.filter(name__iexact=str(province_filter))

            serializer = WeatherForecastSerializer(province,many=True)

            data = serializer.data
            cache.set(path, data, CACHE_TTL)
        return Response(data)

class WeatherView(APIView):
    """
    Lists and adds weathers
    """
    def get(self, request):
        data, path = get_data_from_cache("weather")
        if not data:
            weather = Weather.objects.all()
            serializer = WeatherSerializer(weather,many=True)

            data = serializer.data
            cache.set(path, data, CACHE_TTL)
        return Response(data)

    def post(self, request, format=None):
        serializer = WeatherAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TownView(APIView):
    """
    Lists and adds towns
    """

    def get(self, request):
        data, path = get_data_from_cache("town")

        if not data:
            town = Town.objects.all()
            serializer = TownSerializer(town,many=True)

            data = serializer.data
            cache.set(path, data, CACHE_TTL)
        return Response(data)

    def post(self, request, format=None):
        serializer = TownAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProvinceVeiw(APIView):
    """
    Lists and adds provinces
    """
    def get(self, request):
        data, path = get_data_from_cache("province")

        if not data:
            province = Province.objects.filter(deleted=0).all()
            serializer = ProvinceListSerializer(province,many=True)

            data = serializer.data
            cache.set(path, data, CACHE_TTL)

        return Response(data)

    def post(self, request, format=None):
        serializer = ProvinceAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProvinceDetailWeather(APIView):
    """
    Brings , updates and delete the details of the provinces
    """
    def get_object(self, pk):
        queryset = Province.objects.filter(id=pk).first()
        if not queryset:
            raise Http404
        return queryset

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = ProvinceListSerializer(data)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        filter = self.get_object(pk)
        serializer = ProvinceListSerializer(filter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WeatherDetailWeather(APIView):
    """
    Brings , updates and delete the details of the weather
    """
    def get_object(self, pk):
        queryset = Weather.objects.filter(id=pk).first()
        if not queryset:
            raise Http404
        return queryset

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = WeatherSerializer(data)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        filter = self.get_object(pk)
        serializer = WeatherUpdateSerializer(filter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TownDetailWeather(APIView):
    """
    Brings , updates and delete the details of the town
    """
    def get_object(self, pk):
        queryset = Town.objects.filter(pk=pk).first()
        if not queryset:
            raise Http404
        return queryset

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = TownSerializer(data)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        filter = self.get_object(pk)
        serializer = TownSerializer(filter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)