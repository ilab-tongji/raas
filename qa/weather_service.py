#coding=UTF-8
from service import Service
import requests
from sensor.sensor_service import SensorServiceFactory


class WeatherService(Service):
    def __init__(self):
        super(WeatherService,self).__init__('weather')

    def getWeather(self, entities):
        if entities.get('location') is None:
            weather = self.today_weather()
        else:
            city = 'shanghai'
            if entities['location'][0]['confidence'] > 0.93:
                city = entities['location'][0]['value']
            weather = self.today_weather(city)
        pm = SensorServiceFactory.get_service('get_pm')().get_data()
        r = '天气是'+weather['weather']+',pm2.5的含量为'+pm['pm25']+',pm10的含量为'+pm['pm10']
        return r

    def today_weather(self, city='shanghai', index=0):
        url = 'http://api.map.baidu.com/telematics/v3/weather?location=' + city + '&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback='
        r = requests.get(url)
        data = {}
        data['date'] = r.json()['results'][0]['weather_data'][index]['date']
        data['weather'] = r.json()['results'][0]['weather_data'][index]['weather']
        data['wind'] = r.json()['results'][0]['weather_data'][index]['wind']
        data['temp'] = r.json()['results'][0]['weather_data'][index]['temperature']
        if index == 0:
            data['pm25'] = r.json()['results'][0]['pm25']
            data['wearing'] = r.json()['results'][0]['index'][0]['des']
            data['carwashing'] = r.json()['results'][0]['index'][1]['des']
            data['cold'] = r.json()['results'][0]['index'][2]['des']
            data['sport'] = r.json()['results'][0]['index'][3]['des']
            data['sunshine'] = r.json()['results'][0]['index'][4]['des']
        return data

