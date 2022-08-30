import sys
from jinja2 import Environment, FileSystemLoader
from jsonschema import validate
from yaml import safe_load



# I am opening my schema file
with open('config_data/config_contexts_schemes/dnac9300.local.yml') as file:
    schema = safe_load(file)

# I am opening my data file
with open('config_data/config_contexts/devices/dnac9300.local.yml') as file:
    good_instance = safe_load(file)

# if None is returned validate passess
validate= (validate(good_instance, schema)) # passes
print(validate)

if validate:
    sys.exit(1)

# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/app_hosting.j2')
commands = template.render(config_context=good_instance)
print(commands)
