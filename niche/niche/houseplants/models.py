from django.db import models


# Create your models here.
class Plant(models.Model):
    # english_name = models.CharField(max_length=200)
    # chinese_name = models.CharField(max_length=200)
    # scientific_name = models.CharField(max_length=200)
    # date_purchased = models.DateTimeField('date purchased')
    # full_sun = models.BinaryField(default=0)
    # half_sun = models.BinaryField(default=1)
    # shadow = models.BinaryField(default=0)
    # min_temp = models.IntegerField(default=15)
    # max_temp = models.IntegerField(default=42)
    # comfortable_temp = models.IntegerField(default=25)
    # family = models.CharField(max_length=200)
    # comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.english_name

