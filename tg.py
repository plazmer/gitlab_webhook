import requests
import os


TOKEN = os.getenv('TG_TOKEN')
URL = 'https://api.telegram.org/bot'


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
        send_message(user_id, "🐈Hello {}!\nYour ID is: {}".format(
            user_name,
            user_id))
