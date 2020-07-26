from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.http import JsonResponse, HttpResponse
import json

from .models import Plant, Activity, PlantLog


def index(request):
    plant_list = Plant.objects.order_by('scientific_name')
    watering_list = PlantLog.objects.order_by('date').last
    fertilize_list = PlantLog.objects.order_by('date').last
    context = {'plant_list': plant_list, 'watering_list': watering_list, 'fertilize_list': fertilize_list }
    return render(request, 'houseplants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    last_watering = PlantLog.objects.filter(plant=plant_id, activity='1').order_by('date').last
    last_fertilized = PlantLog.objects.filter(plant=plant_id, activity='2').order_by('date').last
    return render(request, 'houseplants/detail.html', {'plant': plant, 'last_watering': last_watering, 'last_fertilized': last_fertilized})


def log(request):
    log_list = PlantLog.objects.order_by('-date')
    context = {
        'log_list': log_list
        }
    return render(request, 'houseplants/log.html', context)


def activities(request):
    activity_list = Activity.objects.order_by('id')
    context = {
        'activity_list': activity_list
        }
    return render(request, 'houseplants/activities.html', context)


def add_water_log(request, plant_id):
    print("Add Water Getting Called")
    if request.method == 'POST':
        print(f'Plant: {plant_id}')
        # plant = Plant.objects.get(pk=plant_id).scientific_name
        print(now())
        watering = PlantLog(plant=Plant.objects.get(pk=plant_id), date=now(), activity=Activity.objects.get(pk='1'))
        watering.save()
        data = {
            'plant': plant_id,
            'date': now(),
            'activity': '1'
        }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({"error": "Please contact your administrator."}, status=400)


def add_fertilizer_log(request, plant_id):
    if request.method == 'POST':
        fertilizer = PlantLog(plant=Plant.objects.get(pk=plant_id), date=now(), activity=Activity.objects.get(pk='2'))
        fertilizer.save()
        data = {
            'plant': plant_id,
            'date': now(),
            'activity': '1'
        }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({"error": "Please contact your administrator."}, status=400)


def add_plant(request):
    return render(request, 'houseplants/addPlant.html')
