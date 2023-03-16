import json, os
import gitlab, tg, db

"""
Функционал: 
Реакция на телеграмм - 
    /start - вернуть ид
"""


def handler(event, context):
    body = json.loads(event['body'])

    # from telegram
    if body.get("update_id"):
        tg.router(body)

    if body.get("object_kind"):
        repo = body.get('project', {}).get('web_url')

        tpl = gitlab.router(body)
        for tg_id in db.get(repo, body.get("object_kind")):
            tg.send_message(tg_id, tpl, 'HTML')

    return {
        'statusCode': 200,
        'body': 'Ok',
    }
