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


def router(body):
    text = body.get('message', {}).get('text', "")
    user_id = body.get('message', {}).get('chat', {}).get('id')
    user_name = body.get('message', {}).get('chat', {}).get('title')
    if not user_id:
        user_id = body.get('message', {}).get('from', {}).get('id')

    if not user_name:
        user_name = body.get('message', {}).get('from', {}).get('username')

    if text == "/start":
        send_message(user_id, r"🐈(msg: {})\nHello {}!\nYour ID is: {}".format(
            body.get('message', {}).get('message_id'),
            user_name,
            user_id))

    if text.startswith("/register"):
        if user_id != os.getenv('OWNER_ID'):
            send_message(user_id, "who are you?")
            return

        arr = text.split(" ", 4)
        if len(arr) != 5:
            send_message(user_id, "error: received {} params".format(len(arr)))
        else:
            try:
                send_message(user_id, "OK")
            except Exception as exc:
                send_message(user_id, "exception: {}".format(exc))

    if text.startswith("/list"):
        send_message(user_id, "OK")

