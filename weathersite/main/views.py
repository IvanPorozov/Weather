from django.shortcuts import render
from django.http import HttpResponse

import requests

from .forms import CityForm
from .utils import get_weather


def main(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            today_weather, today_afternoon_weather, today_night_weather, tomorrow_morning_weather, \
                tomorrow_afternoon_weather, tomorrow_night_weather, day_after_tomorrow_morning_weather, \
                day_after_tomorrow_afternoon_weather, day_after_tomorrow_night_weather, \
                city = get_weather(form.cleaned_data['city'])
            return render(request, 'main.html', {'form': form, 'weather_description': today_weather[4],
                                                 'temp': today_weather[0], 'temp_feels_like': today_weather[1],
                                                 'temp_min': today_weather[2], 'temp_max': today_weather[3],
                                                 'city': city})
    else:
        form = CityForm()
        today_weather, today_afternoon_weather, today_night_weather, tomorrow_morning_weather, \
            tomorrow_afternoon_weather, tomorrow_night_weather, day_after_tomorrow_morning_weather, \
            day_after_tomorrow_afternoon_weather, day_after_tomorrow_night_weather, \
            city = get_weather('Kiev')
        return render(request, 'main.html', {'form': form, 'weather_description': today_weather[4],
                                             'temp': today_weather[0], 'temp_feels_like': today_weather[1],
                                             'temp_min': today_weather[2], 'temp_max': today_weather[3],
                                             'city': city})
