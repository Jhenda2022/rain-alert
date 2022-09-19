import requests

#How to create TG bot:
#https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

def telegram_bot_sendtext(bot_message):
    bot_token = 'your bot token'
    bot_chatID = 'your chat ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

api_key = "your API key from https://home.openweathermap.org/statistics/onecall_30"

parameters = {
    "lat": 34.977119,
    "lon": 138.383087,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()

#Get the first 12 hours of weather data using slice.
weather_slice = weather_data["hourly"][:12]

#if it rains in the next 12 hours, prompt to bring an umbrella.
will_rain = False
for hour_data in weather_slice:
    weather_list = hour_data["weather"]
    for i in range(12):
        weather_id = weather_list[0]["id"]
        if weather_id < 700:
            will_rain = True
if will_rain:
    test = telegram_bot_sendtext("It's going to rain today. Remember to bring your ☂.")
    print(test)