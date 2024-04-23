import json

import yaml

yaml_file = 'devices.yaml'
json_file = 'lab_envs.json'

with open(yaml_file) as config_file:
    yaml_output = yaml.safe_load(config_file)

with open(json_file) as config_file:
    json_output = json.load(config_file)

for key, value in yaml_output.items():
    lab_env = value['lab_env']
    if lab_env in json_output:
        yaml_output[key]['lab_env'] = {lab_env: json_output.get(lab_env)}
    else:
        yaml_output[key]['lab_env'] = {lab_env: None}


with open('result.yml', 'w') as yaml_file:
    yaml.dump(yaml_output, yaml_file)