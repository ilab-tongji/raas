import requests


def today_weather(city='shanghai', index=0):
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

if __name__ == '__main__':
    city = '%e4%b8%8a%e6%b5%b7'
    index = 1  # 0-today, 1-tomorrow, ... max 3

    print today_weather(city, index)['weather']
