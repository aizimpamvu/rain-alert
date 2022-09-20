import requests
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACdb27db6b252e2c49f25c4b4eee5d2fbc'
auth_token = '3fb8c93be43329e8470aaea7d35bd5f2'
client = Client(account_sid, auth_token)


api_key = "6728aa83cf3ed4614d340873b8f5f464"
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
CRT_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
LAT = -1.95
LONG = 30.0588
EXCLUDE = "alerts, hourly"
parameters = {
    # "lat": LAT,
    # "lon": LONG,
    "q": "Linz",
    "appid": api_key
    # "exclude": "current,minutely,daily"
}

will_rain = False
response = requests.get(CRT_Endpoint, params=parameters)
print(response.status_code)
weather_slice = response.json()["weather"][:5]
print(weather_slice[0])
for current_weather in weather_slice:
    condition_code =current_weather["id"]

    if condition_code <700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body='Hi Alleluia, will rain bring  unumbrella☂️',
        from_='+15304664309',
        to='+250788208941'
    )
    print(message.status)

