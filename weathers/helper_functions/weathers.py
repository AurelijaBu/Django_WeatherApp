import requests

def get_weather_data(latitude: float, longitude: float):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,wind_direction_10m,relative_humidity_2m,cloud_cover,precipitation'

    response = requests.get(url)
    data = response.json()

    weather = {
        'temperature': data['current']['temperature_2m'],
        'wind_speed': data['current']['wind_speed_10m'],
        'humidity': data['current']['relative_humidity_2m'],
        'cloud_cover': data['current']['cloud_cover'],
        'precipitation': data['current']['precipitation']
    }

    return weather