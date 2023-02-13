import sys
from jinja2 import Environment, FileSystemLoader
from jsonschema import validate
from yaml import safe_load


# I am opening my data file
with open('config_context/devices/r3.yml') as file:
    data_file = safe_load(file)


# I am opening my schema file
with open('schema/router.yml') as file:
    schema = safe_load(file)

# if None is returned validate passess
validate= (validate(data_file, schema)) # passes
print(validate)

if validate != None:
    sys.exit(validate)


# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/ike_phase_1.j2')
commands = template.render(data=data_file)
print(commands)

# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/ike_keys.j2')
commands = template.render(data=data_file)
print(commands)

# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/ike_phase_2.j2')
commands = template.render(data=data_file)
print(commands)

# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/standard_acl.j2')
commands = template.render(data=data_file)
print(commands)

# This is combining my data file with the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/crypto_map.j2')
commands = template.render(data=data_file)
print(commands)