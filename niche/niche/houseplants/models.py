from django.db import models
from datetime import date


# Create your models here.
class Plant(models.Model):
    # english_name = models.TextField(default="", max_length=200)
    # chinese_name = models.TextField(default="", max_length=200)
    scientific_name = models.TextField(max_length=200)
    # date_purchased = models.DateTimeField('date purchased')
    # full_sun = models.BooleanField(default=False)
    # half_sun = models.BooleanField(default=False)
    # shadow = models.BooleanField(default=False)
    # min_temp = models.IntegerField(default=15)
    # max_temp = models.IntegerField(default=42)
    # comfortable_temp = models.IntegerField(default=25)
    # family = models.TextField(default="", max_length=200)
    # comments = models.TextField(default="", max_length=1000)

    def __str__(self):
        return self.scientific_name


# Keeping Track of the different possible activities.
class Activity(models.Model):
    name = models.TextField(default=" ", max_length=50)
    description = models.TextField(default="Activity Description", max_length=200)

    def __str__(self):
        return self.name


# Tracking information about the plants.
class PlantLog(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.date, self.plant, self.activity)
    
    class Meta:
        ordering = ['date']

    
