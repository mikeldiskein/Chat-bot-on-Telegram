import requests as r
import json
import time

import const


def answer_user_bot(data, user_id):
    url = const.URL.format(
        token=const.TOKEN,
        method=const.SEND_METH
    )
    data = {
        'chat_id': user_id,   # тут я неплохо догадался, что можно вытащить id конкретного юзера)
        'text': data
    }

    r.post(url, data)


def parse_weather_data(data):
    weather_state = None
    for elem in data['weather']:
        weather_state = elem['main']
    temp = round(data['main']['temp'] - 273.15)
    city = data['name']
    wind = data['wind']['speed']
    msg = f'Погода в {city}: температура {temp}, общее состояние погоды: {weather_state}, скорость ветра {wind} м/с'
    return msg


def get_weather(location):
    url = const.WEATHER_URL.format(city=location, token=const.WEATHER_TOKEN)
    response = r.get(url)
    if response.status_code != 200:
        return 'city not found'
    data = json.loads(response.content)

    return parse_weather_data(data)


def get_message(data):
    return data['message']['text']


def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    const.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATES_METH)
        content = r.get(url).text

        data = json.loads(content)
        result = data['result'][::-1]
        needed_part = result[0]
        user_id = needed_part['message']['chat']['id']

        url_0 = const.URL.format(token=const.TOKEN, method=const.SEND_METH)
        first_hello = {
            'chat_id': user_id,
            'text': 'Привет! Чтобы узнать погоду в любом городе, просто напиши название этого города! Но ничего другого'
                    ' писать не нужно, потому что больше пока я ничего не умею :)'
        }

        if const.UPDATE_ID != needed_part['update_id']:
            save_update_id(needed_part)
            message = get_message(needed_part)
            if message == '/start':
                r.post(url_0, first_hello)
            else:
                msg = get_weather(message)
                answer_user_bot(msg, user_id)
                print(needed_part['message'])

        time.sleep(1)


if __name__ == '__main__':
  main()

