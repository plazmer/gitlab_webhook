import json, os
import requests
import gitlab

"""
Функционал: 
Реакция на телеграмм - 
    /start - вернуть ид
"""





def handler(event, context):
    body = json.loads(event['body'])

    # from telegram
    if body.get("update_id"):
        tg(body)

    return {
        'statusCode': 200,
        'body': 'Ok',
    }


def tg_send_message(chat_id, text, parse_mode=None):
    print("send " + text)
    data = {"chat_id": chat_id, "text": text}
    if parse_mode:
        data["parse_mode"] = parse_mode

    r = requests.post("https://api.telegram.org/bot{}/sendMessage".format(os.environ.get("TG_TOKEN")), data=data)
    r.raise_for_status()


def tg(body):
    text = body.get('message', {}).get('text', "")
    user_id = body.get('message', {}).get('chat', {}).get('id')
    user_name = body.get('message', {}).get('chat', {}).get('title')
    if not user_id:
        user_id = body.get('message', {}).get('from', {}).get('id')

    if not user_name:
        user_name = body.get('message', {}).get('from', {}).get('username')

    if text == "/start":
        tg_send_message(user_id, "🐈Hello {}!\nYour ID is: {}".format(
            body.get('message', {}).get('message_id'),
            user_name,
            user_id))

