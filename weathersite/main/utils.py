import requests


def get_weather(city):
    api_key = '2f2aaa0c2b730c56175db762af7f813b'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temp = round(data['main']['temp'] - 273.15)
        temp_feels_like = round(data['main']['feels_like'] - 273.15)
        temp_min = round(data['main']['temp_min'] - 273.15)
        temp_max = round(data['main']['temp_max'] - 273.15)
        city = data['name']
        return weather_description, temp, temp_feels_like, temp_min, temp_max, city
    else:
        return 'City not found'
