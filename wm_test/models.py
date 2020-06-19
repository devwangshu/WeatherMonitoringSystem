# Create your models here.
from datetime import datetime
from django.db import models

class Setting(models.Model):
    ip_address = models.CharField(max_length=40, blank=False, null=True)
    wd_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    wd_unit = models.CharField(max_length=10, blank=False, null=True)
    ws_sensor_name = models.CharField(max_length=15, blank=False, null=True)
    ws_unit = models.CharField(max_length=10, blank=False, null=True)
    rg_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    rg_unit = models.CharField(max_length=10, blank=False, null=True)
    pm2_5_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    pm2_5_unit = models.CharField(max_length=10, blank=False, null=True)
    pm10_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    pm10_unit = models.CharField(max_length=10, blank=False, null=True)
    humidity_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    humidity_unit = models.CharField(max_length=10, blank=False, null=True)
    temperature_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    temperature_unit = models.CharField(max_length=10, blank=False, null=True)
    so2_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    so2_unit = models.CharField(max_length=10, blank=False, null=True)
    co_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    co_unit = models.CharField(max_length=10, blank=False, null=True)
    no2_sensor_name = models.CharField(max_length=100, blank=False, null=True)
    no2_unit = models.CharField(max_length=10, blank=False, null=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True, blank=False, null=True)
    modified_date = models.DateField(auto_now=False, auto_now_add=True, blank=False, null=True)

    class Meta:
        db_table = "Setting"


class AddSensor(models.Model):
    sensor_id = models.CharField(max_length=200,blank=False, null=True)
    sensor_name=models.CharField(max_length=200,blank=False, null=True)
    sensor_unit= models.CharField(max_length=200,blank=False, null=True)
    min_range = models.CharField(max_length=200,blank=False, null=True)
    max_range = models.CharField(max_length=200,blank=False, null=True)
    desc = models.CharField(max_length=200,blank=False, null=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "AddSensor"


class Weather_data(models.Model):
    setting_id = models.IntegerField(blank=False, null=True)
    rain_gauge=models.CharField(max_length=200, blank=False, null=True)
    pm2_5= models.CharField(max_length=200, blank=False, null=True)
    pm10 = models.CharField(max_length=200, blank=False, null=True)
    humidity = models.CharField(max_length=200, blank=False, null=True)
    temperature = models.CharField(max_length=200, blank=False, null=True)
    ws_value = models.CharField(max_length=200, blank=False, null=True)
    wd_value = models.CharField(max_length=200, blank=False, null=True)
    no2 = models.CharField(max_length=200, blank=False, null=True)
    co = models.CharField(max_length=200, blank=False, null=True)
    so2 = models.CharField(max_length=200, blank=False, null=True)
    date = models.DateField(auto_now=False, auto_now_add=True, blank=False, null=True)
    time= models.TimeField(auto_now=False, auto_now_add=True, blank=False, null=True)

    created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Weather_data"


