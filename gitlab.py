from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("views/"))


def router(j):
    name = j.get('event_name')
    repo = j.get('project', {}).get('web_url')

    tpl = template(name + '.html', j=j)
