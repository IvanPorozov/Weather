from datetime import datetime

import requests

api_key = '2f2aaa0c2b730c56175db762af7f813b'

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}



def get_weather(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        city = data['name']
        temp = round(data['main']['temp'] - 273.15)
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        four_days_url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
        four_days_response = requests.get(four_days_url)
        four_days_data = four_days_response.json()

        # Today
        today_weather = (
            round(four_days_data['list'][0]['main']['temp'] - 273.15),
            round(four_days_data['list'][0]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][0]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][0]['main']['temp_max'] - 273.15),
            four_days_data['list'][0]['weather'][0]['description']
        )

        today_afternoon_weather = (
            round(four_days_data['list'][2]['main']['temp'] - 273.15),
            round(four_days_data['list'][2]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][2]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][2]['main']['temp_max'] - 273.15),
            four_days_data['list'][2]['weather'][0]['description']
        )

        today_night_weather = (
            round(four_days_data['list'][4]['main']['temp'] - 273.15),
            round(four_days_data['list'][4]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][4]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][4]['main']['temp_max'] - 273.15),
            four_days_data['list'][4]['weather'][0]['description']
        )

        # Tomorrow
        tomorrow_morning_weather = (
            round(four_days_data['list'][8]['main']['temp'] - 273.15),
            round(four_days_data['list'][8]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][8]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][8]['main']['temp_max'] - 273.15),
            four_days_data['list'][8]['weather'][0]['description']
        )

        tomorrow_afternoon_weather = (
            round(four_days_data['list'][10]['main']['temp'] - 273.15),
            round(four_days_data['list'][10]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][10]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][10]['main']['temp_max'] - 273.15),
            four_days_data['list'][10]['weather'][0]['description']
        )

        tomorrow_night_weather = (
            round(four_days_data['list'][12]['main']['temp'] - 273.15),
            round(four_days_data['list'][12]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][12]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][12]['main']['temp_max'] - 273.15),
            four_days_data['list'][12]['weather'][0]['description']
        )

        # Day after tomorrow
        day_after_tomorrow_morning_weather = (
            round(four_days_data['list'][16]['main']['temp'] - 273.15),
            round(four_days_data['list'][16]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][16]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][16]['main']['temp_max'] - 273.15),
            four_days_data['list'][16]['weather'][0]['description']
        )

        day_after_tomorrow_afternoon_weather = (
            round(four_days_data['list'][18]['main']['temp'] - 273.15),
            round(four_days_data['list'][18]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][18]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][18]['main']['temp_max'] - 273.15),
            four_days_data['list'][18]['weather'][0]['description']
        )

        day_after_tomorrow_night_weather = (
            round(four_days_data['list'][20]['main']['temp'] - 273.15),
            round(four_days_data['list'][20]['main']['feels_like'] - 273.15),
            round(four_days_data['list'][20]['main']['temp_min'] - 273.15),
            round(four_days_data['list'][20]['main']['temp_max'] - 273.15),
            four_days_data['list'][20]['weather'][0]['description']
        )

        return today_weather, today_afternoon_weather, today_night_weather, tomorrow_morning_weather, \
            tomorrow_afternoon_weather, tomorrow_night_weather, day_after_tomorrow_morning_weather, \
            day_after_tomorrow_afternoon_weather, day_after_tomorrow_night_weather, temp, city

    else:
        return None, None, None, None, None, None, None, None, None, None, 'City not found'


def get_current_date():
    date = datetime.now()
    month = months.get(date.month)
    tomorrow = date.day + 1
    day_after_tomorrow = date.day + 2
    return date.day, tomorrow, day_after_tomorrow, month
