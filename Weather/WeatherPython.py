import requests
print ("Введите город")
city = input()
print ("Введите код страны на английском. Можете ничего не вводить")
code = input()
city += ", " + code 
id = "63c11595b601e61275ec878025b3593b"
response = (requests.get("http://api.openweathermap.org/data/2.5/weather",
                params = {'q': city, 'units' : 'metric','lang' : 'ru', 'appid' : id}))
data = response.json()
print ('Город: ', data['name'])
print ('Код страны: ', data['sys']['country'])
print ('Погода: ', data['weather'][0]['description'])
print ('Температура: ', data['main']['temp'], '°C')
print ('Скорость ветра: ', data['wind']['speed'], ' м/c')
