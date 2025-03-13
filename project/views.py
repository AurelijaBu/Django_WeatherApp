from django.shortcuts import render
from weathers.models import City
from django.http import JsonResponse
from weathers.helper_functions.weathers import get_weather_data


def home(request):
    cities = City.objects.all()
    for city in cities:
        weather_data = get_weather_data(city.coordination_x, city.coordination_y)
        city.temperature = weather_data.get('temperature')

    context = {'cities' : cities[:4]}
    return render(request, 'home.html', context)


def get_weather_data_view(request):
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')

    if latitude and longitude:
        weather = get_weather_data(float(latitude), float(longitude))
        return JsonResponse(weather)

    return JsonResponse({'error': 'No coordinates provided'}, status=400)