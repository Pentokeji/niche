from django.contrib import admin

from .models import Plant, Activity, PlantLog

# Register your models here.
admin.site.register(Plant),
admin.site.register(Activity),
admin.site.register(PlantLog)
