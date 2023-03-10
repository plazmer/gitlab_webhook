from jinja2 import Environment, FileSystemLoader
import os

def router(j, directory = ""):
    environment = Environment(loader=FileSystemLoader(os.path.join(directory, "views/")))
    name = j.get("object_kind", "")

    template = environment.get_template(name+".html")
    response = template.render(j=j)

    return response
