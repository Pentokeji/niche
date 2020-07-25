from django.db import models


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
