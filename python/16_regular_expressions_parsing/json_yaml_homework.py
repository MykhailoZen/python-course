import json
import yaml
import pathlib

file_json = pathlib.Path('lab_envs.json')
with open(file_json, 'r') as file:
    lab_envs = json.load(file)
    # print(lab_envs.items())

file_yaml = pathlib.Path('devices.yaml')
with open(file_yaml, 'r') as stream:
    devices = yaml.safe_load(stream)
    # print(devices.items())
    # print(devices['knight-lamar']['lab_env'])

devices_with_envs = pathlib.Path('devices_with_envs.yaml')
for device, device_info in devices.items():
    lab_env = device_info['lab_env']
    # print(lab_env)
    if lab_env in lab_envs:
        device_info['lab_env'] = lab_envs.get(lab_env)
    else:
        device_info['lab_env'] = None

with open(devices_with_envs, 'w') as output:
    yaml.dump(devices, output, indent=4)
