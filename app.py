from bottle import get, post, request, run, template
import tg, db
import jinja2


@get("/")
def index():
    return "Ok"


@post("/gitlab")
def gitlab():
    j = request.json
    if not j:
        return "error"

    name = j.get('event_name')
    repo = j.get('project',{}).get('web_url')

    tpl = template(name + '.html', j=j)

    for tg_id in db.settings.get(repo, []):
        tg.send_message(tg_id, tpl, 'HTML')
    return "Ok"


run(host='0.0.0.0', port=7000, debug=True)
