from jinja2 import Environment, FileSystemLoader
from yaml import safe_load


# I am opening my data file
with open('config_context/devices/dnac9300.local.yml') as file:
    app = safe_load(file)

# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/app_hosting.j2')
commands = template.render(config_context=app)
print(commands)
