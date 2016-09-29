from django.db import models

# Create your models here.

class Zone(models.Model):
    zone_name = models.CharField(max_length=200)


class Room(models.Model):
    room_name = models.CharField(max_length=200)


class TemperatureRecord(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    record_time = models.DateTimeField('Time of reading')
    temperature = models.FloatField()
    

class Program(models.Model):
    weekday = models.IntegerField()
    on_time = models.TimeField()
    off_time = models.TimeField()
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    set_temp = models.FloatField()

class ZoneRecord(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    record_time = models.DateTimeField()
    heating_on = models.BooleanField()



