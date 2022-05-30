from weather.enums import *
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.cache import cache

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    deleted = models.IntegerField(default=0,null=True,blank=True)

    class Meta:
        abstract = True

class Province(BaseModel):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'province'
    def __str__(self):
        return f'{self.name}'

@receiver(post_save, sender=Province)
def clear_cache(instance, **kwargs):
    path = settings.CACHE_KEY_PATH.format("province")
    keys = cache.keys('*')
    if keys:
        cache.delete_many(keys)

class Town(BaseModel):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province,related_name='town', on_delete=models.CASCADE)
    class Meta:
        db_table = 'town'


@receiver(post_save, sender=Town)
def clear_cache(instance, **kwargs):
    path = settings.CACHE_KEY_PATH.format("town")
    keys = cache.keys('*')
    if keys:
        cache.delete_many(keys)

class Weather(BaseModel):

    weather_forecast = models.CharField(max_length=100)
    degree = models.FloatField(default=0)

    province = models.ForeignKey(Province,related_name='province_weather', on_delete=models.CASCADE, null=True, blank=True, default=None)
    town = models.ForeignKey(Town,related_name='town_weather', on_delete=models.CASCADE, null=True, blank=True, default=None)
    class Meta:
        db_table = 'weather'

@receiver(post_save, sender=Weather)
def clear_cache(instance, **kwargs):
    path = settings.CACHE_KEY_PATH.format("weather")
    keys = cache.keys('*')
    if keys:
        cache.delete_many(keys)