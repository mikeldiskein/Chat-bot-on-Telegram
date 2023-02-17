TOKEN = '5388778375:AAGKmK1wvzLWPVRFWIr0LOFf3zNx7pa7yG0'
URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATES_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 1563279921

UPDATE_ID_FILE_PATH = 'update_id.py'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data



WEATHER_TOKEN = '72289c023ae0af89b8c7d7bab71ba28c'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'



