from django.urls import path

from . import views

app_name = 'houseplants'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:plant_id>/', views.detail, name='detail'),
	path('log', views.log, name='log'),
	path('activities', views.activities, name='activities'),
	path('<int:plant_id>/watering', views.add_water_log, name='water'),
	path('<int:plant_id>/fertilizing', views.add_fertilizer_log, name='fertilize'),
	path('add_plant', views.add_plant, name='add-plant')
]
