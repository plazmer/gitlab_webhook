import requests
import os
import time

TOKEN = os.getenv('TG_TOKEN')
URL = 'https://api.telegram.org/bot'


def get_updates(offset=0):
    url = f'{URL}{TOKEN}/getUpdates?offset={offset}'
    result = requests.get(url).json()
    print(result)
    return result['result']


def send_message(chat_id, text, parse_mode=None):
    print("send " + text)
    data = {"chat_id": chat_id, "text": text}
    if parse_mode:
        data["parse_mode"] = parse_mode

    r = requests.post("https://api.telegram.org/bot{}/sendMessage".format(os.getenv("TG_TOKEN")), data=data)
    r.raise_for_status()


def check_message(chat_id, message):
    for mes in message.lower().replace(',', '').split():
        if mes in ['привет', 'ку']:
            send_message(chat_id, 'Привет :)')
        if mes in ['дела?', 'успехи?']:
            send_message(chat_id, 'Спасибо, хорошо!')


def run():
    update_id = get_updates()[-1]['update_id']  # Присваиваем ID последнего отправленного сообщения боту
    while True:
        time.sleep(2)
        messages = get_updates(update_id)  # Получаем обновления
        for message in messages:
            # Если в обновлении есть ID больше чем ID последнего сообщения, значит пришло новое сообщение
            if update_id < message['update_id']:
                update_id = message['update_id']  # Присваиваем ID последнего отправленного сообщения боту
                # Отвечаем тому кто прислал сообщение боту
                check_message(message['message']['chat']['id'], message['message']['text'])


def tg(body):
    text = body.get('message', {}).get('text', "")
    user_id = body.get('message', {}).get('chat', {}).get('id')
    user_name = body.get('message', {}).get('chat', {}).get('title')
    if not user_id:
        user_id = body.get('message', {}).get('from', {}).get('id')

    if not user_name:
        user_name = body.get('message', {}).get('from', {}).get('username')

    if text == "/start":
        tg_send_message(user_id, r"🐈(msg: {})\nHello {}!\nYour ID is: {}".format(
            body.get('message', {}).get('message_id'),
            user_name,
            user_id))

    if text.startswith("/register"):
        if user_id != os.getenv('OWNER_ID'):
            tg_send_message(user_id, "who are you?")
            return

        arr = text.split(" ", 4)
        if len(arr) != 5:
            tg_send_message(user_id, "error: received {} params".format(len(arr)))
        else:
            try:
                tg_send_message(user_id, "OK")
            except Exception as exc:
                tg_send_message(user_id, "exception: {}".format(exc))

    if text.startswith("/list"):
        tg_send_message(user_id, "OK")


if __name__ == '__main__':
    run()
