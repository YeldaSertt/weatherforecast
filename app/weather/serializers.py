from rest_framework import serializers
from weather.models import Province, Town , Weather

class ProvinceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ['name','id']
        read_only_field = ['crated_at']

    def update(self,instance,validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.save()
        return instance

class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = ["name" , 'province']

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.province = validated_data.get("province", instance.province)
        instance.save()
        return instance

class WeatherSerializer(serializers.ModelSerializer):
    town = serializers.CharField(source="town.name", allow_null=True)
    class Meta:
        model = Weather
        exclude = ['created_at', 'updated_at', 'deleted','id']
        read_only_field = ['crated_at','id',"town"]
        #fields = '__all__'

class WeatherUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        exclude = ['created_at', 'updated_at', 'deleted','id']
        read_only_field = ['crated_at']

    def update(self,instance,validated_data):
        instance.degree=validated_data.get("degree",instance.degree)
        instance.weather_forecast=validated_data.get("weather_forecast", instance.weather_forecast)
        instance.town = validated_data.get("town", instance.town)
        instance.save()
        return instance

class WeatherAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        exclude = ['created_at', 'updated_at', 'deleted','id']

class ProvinceAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class WeatherForecastSerializer(serializers.ModelSerializer):
    degree = serializers.SerializerMethodField()
    province_weather = WeatherSerializer(many=True, allow_null=False)
    class Meta:
        model = Province
        fields = ['name','degree', 'province_weather' ]

    def get_degree(self, obj):
        weather = obj.province_weather.filter(town__isnull=True).first()
        if not weather:
            return 0
        return weather.degree

class TownAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = '__all__'