from django.shortcuts import render, get_object_or_404, redirect
from .models import City, CityWeathers
from project.views import get_weather_data


def index(request):
    """
    Displays a list of all available cities.

    :param request: HTTP request object.
    :return: Rendered HTML page showing all cities.
    """
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request=request, template_name='weathers/cities.html', context=context)


def detail(request, city_name):
    """
    Displays detailed weather information for a specific city. If the city does not exist,
    redirects to the cities list page. Also saves the fetched weather data to the database.

    :param request: HTTP request object.
    :param city_name: Name of the city to retrieve weather data for.
    :return: Rendered HTML page showing weather data for the selected city.
    """
    city = None
    try:
        city = City.objects.get(name=city_name)
    except City.DoesNotExist:
        return redirect('cities')

    weather_data = get_weather_data(city.coordination_x, city.coordination_y)

    city_weathers = CityWeathers.objects.create(
        city=city,
        temperature=weather_data.get('temperature', None)
    )
    city_weathers.save()

    context = {
        'city': city,
        'weather': weather_data,
    }

    return render(request, 'weathers/city.html', context)


def weathers_data(request):
    """
    Displays all weather records stored in the database for all cities.

    :param request: HTTP request object.
    :return: Rendered HTML page listing weather data for all cities.
    """
    cities_weather = CityWeathers.objects.all()
    context = {'cities': cities_weather}
    return render(request=request, template_name='weathers/weathers_data.html', context=context)


def add_city(request):
    """
    Handles the form for adding a new city. On POST request, saves the new city to the database.

    :param request: HTTP request object.
    :return: Redirects to the cities list after saving, or renders the city form on GET request.
    """
    if request.method == 'POST':
        city = City.objects.create(
            name=request.POST['city'],
            country=request.POST['country'],
            coordination_x=request.POST['coordination_x'],
            coordination_y=request.POST['coordination_y'],
            image=request.FILES.get('image'),
        )
        city.save()
        return redirect('cities')

    context = {}
    return render(request=request, template_name='weathers/add_city.html', context=context)


def delete_city(request, city_name):
    """
    Deletes a specific city from the database based on the city name.

    :param request: HTTP request object.
    :param city_name: Name of the city to delete.
    :return: Redirects to the cities list after deletion.
    """
    city = get_object_or_404(City, name=city_name)
    city.delete()
    return redirect('cities')


def update_city(request, city_name):
    """
    Handles updating information for a specific city. On POST request, saves the updated data.

    :param request: HTTP request object.
    :param city_name: Name of the city to update.
    :return: Redirects to the cities list after update, or renders the update form on GET request.
    """
    city = get_object_or_404(City, name=city_name)

    if request.method == 'POST':
        city.name = request.POST['city']
        city.country = request.POST['country']
        city.coordination_x = request.POST['coordination_x']
        city.coordination_y = request.POST['coordination_y']

        if 'image' in request.FILES:
            city.image = request.FILES['image']

        city.save()
        return redirect('cities')

    context = {'city': city}
    return render(request, 'weathers/update_city.html', context)




