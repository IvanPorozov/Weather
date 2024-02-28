from django.shortcuts import render
from django.http import HttpResponse

import requests

from .forms import CityForm
from .utils import get_weather


def main(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            weather_description, temp, temp_feels_like, temp_min, \
                temp_max, city = get_weather(form.cleaned_data['city'])
            return render(request, 'main.html', {'form': form, 'weather_description': weather_description,
                                                 'temp': temp, 'temp_feels_like': temp_feels_like,
                                                 'temp_min': temp_min, 'temp_max': temp_max, 'city': city})
    else:
        form = CityForm()
        weather_description, temp, temp_feels_like, temp_min, \
            temp_max, city = get_weather('Kiev')
        return render(request, 'main.html', {'form': form, 'weather_description': weather_description,
                                             'temp': temp, 'temp_feels_like': temp_feels_like,
                                             'temp_min': temp_min, 'temp_max': temp_max, 'city': city})
