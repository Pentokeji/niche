from django.shortcuts import render, get_object_or_404

from .models import Plant


def index(request):
    plant_list = Plant.objects.order_by('scientific_name')
    context = {'plant_list': plant_list}
    return render(request, 'houseplants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'houseplants/detail.html', {'plant': plant})