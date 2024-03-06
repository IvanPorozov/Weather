from django.shortcuts import render

from .forms import CityForm
from .utils import *


def main(request):
    day, tomorrow, day_after_tomorrow, month = get_current_date()
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            today_weather, today_afternoon_weather, today_night_weather, tomorrow_morning_weather, \
                tomorrow_afternoon_weather, tomorrow_night_weather, day_after_tomorrow_morning_weather, \
                day_after_tomorrow_afternoon_weather, day_after_tomorrow_night_weather, temp, sunrise, sunset, \
                wind_speed, gust, pressure, humidity, city = get_weather(form.cleaned_data['city'])
            return render(request, 'main.html',
                          {'form': form, 'today_weather_description': today_weather[4],
                           'today_temp': today_weather[0], 'today_temp_feels_like': today_weather[1],
                           'today_temp_min': today_weather[2], 'today_temp_max': today_weather[3],

                           'today_afternoon_weather_description': today_afternoon_weather[4],
                           'today_afternoon_temp': today_afternoon_weather[0],
                           'today_afternoon_temp_feels_like': today_afternoon_weather[1],
                           'today_afternoon_temp_min': today_afternoon_weather[2],
                           'today_afternoon_temp_max': today_afternoon_weather[3],

                           'today_night_weather_description': today_night_weather[4],
                           'today_night_temp': today_night_weather[0],
                           'today_night_temp_feels_like': today_night_weather[1],
                           'today_night_temp_min': today_night_weather[2],
                           'today_night_temp_max': today_night_weather[3],
                           #  Tomorrow
                           'tomorrow_weather_description': tomorrow_morning_weather[4],
                           'tomorrow_temp': tomorrow_morning_weather[0],
                           'tomorrow_temp_feels_like': tomorrow_morning_weather[1],
                           'tomorrow_temp_min': tomorrow_morning_weather[2],
                           'tomorrow_temp_max': tomorrow_morning_weather[3],

                           'tomorrow_afternoon_weather_description': tomorrow_afternoon_weather[4],
                           'tomorrow_afternoon_temp': tomorrow_afternoon_weather[0],
                           'tomorrow_afternoon_temp_feels_like': tomorrow_afternoon_weather[1],
                           'tomorrow_afternoon_temp_min': tomorrow_afternoon_weather[2],
                           'tomorrow_afternoon_temp_max': tomorrow_afternoon_weather[3],

                           'tomorrow_night_weather_description': tomorrow_night_weather[4],
                           'tomorrow_night_temp': tomorrow_night_weather[0],
                           'tomorrow_night_temp_feels_like': tomorrow_night_weather[1],
                           'tomorrow_night_temp_min': tomorrow_night_weather[2],
                           'tomorrow_night_temp_max': tomorrow_night_weather[3],
                           #  Day after tomorrow
                           'dat_weather_description': day_after_tomorrow_morning_weather[4],
                           'dat_temp': day_after_tomorrow_morning_weather[0],
                           'dat_temp_feels_like': day_after_tomorrow_morning_weather[1],
                           'dat_temp_min': day_after_tomorrow_morning_weather[2],
                           'dat_temp_max': day_after_tomorrow_morning_weather[3],

                           'dat_afternoon_weather_description': day_after_tomorrow_afternoon_weather[4],
                           'dat_afternoon_temp': day_after_tomorrow_afternoon_weather[0],
                           'dat_afternoon_temp_feels_like': day_after_tomorrow_afternoon_weather[1],
                           'dat_afternoon_temp_min': day_after_tomorrow_afternoon_weather[2],
                           'dat_afternoon_temp_max': day_after_tomorrow_afternoon_weather[3],

                           'dat_night_weather_description': day_after_tomorrow_night_weather[4],
                           'dat_night_temp': day_after_tomorrow_night_weather[0],
                           'dat_night_temp_feels_like': day_after_tomorrow_night_weather[1],
                           'dat_night_temp_min': day_after_tomorrow_night_weather[2],
                           'dat_night_temp_max': day_after_tomorrow_night_weather[3],

                           'wind_speed': wind_speed, 'gust': gust, 'pressure': pressure, 'humidity': humidity,

                           'temp': temp, 'sunrise': sunrise, 'sunset': sunset, 'city': city, 'day': day,
                           'tomorrow': tomorrow, 'dat': day_after_tomorrow, 'month': month
                           })
    else:
        form = CityForm()
        today_weather, today_afternoon_weather, today_night_weather, tomorrow_morning_weather, \
            tomorrow_afternoon_weather, tomorrow_night_weather, day_after_tomorrow_morning_weather, \
            day_after_tomorrow_afternoon_weather, day_after_tomorrow_night_weather, temp, sunrise, sunset, \
            wind_speed, gust, pressure, humidity, city = get_weather('Kiev')
        return render(request, 'main.html',
                      {'form': form, 'today_weather_description': today_weather[4],
                       'today_temp': today_weather[0], 'today_temp_feels_like': today_weather[1],
                       'today_temp_min': today_weather[2], 'today_temp_max': today_weather[3],

                       'today_afternoon_weather_description': today_afternoon_weather[4],
                       'today_afternoon_temp': today_afternoon_weather[0],
                       'today_afternoon_temp_feels_like': today_afternoon_weather[1],
                       'today_afternoon_temp_min': today_afternoon_weather[2],
                       'today_afternoon_temp_max': today_afternoon_weather[3],

                       'today_night_weather_description': today_night_weather[4],
                       'today_night_temp': today_night_weather[0],
                       'today_night_temp_feels_like': today_night_weather[1],
                       'today_night_temp_min': today_night_weather[2],
                       'today_night_temp_max': today_night_weather[3],
                       #  Tomorrow
                       'tomorrow_weather_description': tomorrow_morning_weather[4],
                       'tomorrow_temp': tomorrow_morning_weather[0],
                       'tomorrow_temp_feels_like': tomorrow_morning_weather[1],
                       'tomorrow_temp_min': tomorrow_morning_weather[2],
                       'tomorrow_temp_max': tomorrow_morning_weather[3],

                       'tomorrow_afternoon_weather_description': tomorrow_afternoon_weather[4],
                       'tomorrow_afternoon_temp': tomorrow_afternoon_weather[0],
                       'tomorrow_afternoon_temp_feels_like': tomorrow_afternoon_weather[1],
                       'tomorrow_afternoon_temp_min': tomorrow_afternoon_weather[2],
                       'tomorrow_afternoon_temp_max': tomorrow_afternoon_weather[3],

                       'tomorrow_night_weather_description': tomorrow_night_weather[4],
                       'tomorrow_night_temp': tomorrow_night_weather[0],
                       'tomorrow_night_temp_feels_like': tomorrow_night_weather[1],
                       'tomorrow_night_temp_min': tomorrow_night_weather[2],
                       'tomorrow_night_temp_max': tomorrow_night_weather[3],
                       #  Day after tomorrow
                       'dat_weather_description': day_after_tomorrow_morning_weather[4],
                       'dat_temp': day_after_tomorrow_morning_weather[0],
                       'dat_temp_feels_like': day_after_tomorrow_morning_weather[1],
                       'dat_temp_min': day_after_tomorrow_morning_weather[2],
                       'dat_temp_max': day_after_tomorrow_morning_weather[3],

                       'dat_afternoon_weather_description': day_after_tomorrow_afternoon_weather[4],
                       'dat_afternoon_temp': day_after_tomorrow_afternoon_weather[0],
                       'dat_afternoon_temp_feels_like': day_after_tomorrow_afternoon_weather[1],
                       'dat_afternoon_temp_min': day_after_tomorrow_afternoon_weather[2],
                       'dat_afternoon_temp_max': day_after_tomorrow_afternoon_weather[3],

                       'dat_night_weather_description': day_after_tomorrow_night_weather[4],
                       'dat_night_temp': day_after_tomorrow_night_weather[0],
                       'dat_night_temp_feels_like': day_after_tomorrow_night_weather[1],
                       'dat_night_temp_min': day_after_tomorrow_night_weather[2],
                       'dat_night_temp_max': day_after_tomorrow_night_weather[3],

                       'wind_speed': wind_speed, 'gust': gust, 'pressure': pressure, 'humidity': humidity,

                       'temp': temp, 'sunrise': sunrise, 'sunset': sunset, 'city': city, 'day': day,
                       'tomorrow': tomorrow, 'dat': day_after_tomorrow, 'month': month
                       })
