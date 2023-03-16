import json
import db
import gitlab
import tg
from bottle import get, post, request, run


@get("/")
def index():
    return "Ok"


@post("/gitlab")
def gitlab_post():
    j = request.json
    if not j:
        return "error"

    repo = j.get('project', {}).get('web_url')

    tpl = gitlab.router(j)

    for tg_id in db.get(repo, j.get("object_kind")):
        tg.send_message(tg_id, tpl, 'HTML')
    return "Ok"


@get("/gitlab_test")
def gitlab_test():
    ev = request.query["event"]
    with open("tests/" + ev + ".json", "r") as f:
        j = json.load(f)
        if not j:
            return "error"

    tpl = gitlab.router(j).replace('\n', '<br/>\n')
    return tpl


run(host='0.0.0.0', port=7000, debug=True)
