#2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file,
# which has "lab_env" attribute filled for each device.
# If there is no such env in the lab_envs.json, set it for the corresponding device to None.

import json
import yaml

# Given files
devices_yaml = 'devices.yaml'
envs_json = 'lab_envs.json'
new_file = 'new_file.yaml'

# Info from YAML file
with open(devices_yaml, 'r') as file:
    devices_data = yaml.safe_load(file)

# Info from JSON file
with open(envs_json, 'r') as file:
    lab_envs_data = json.load(file)

# Updating info
for device, info in devices_data.items():
    if info['lab_env'] in lab_envs_data:
        info['lab_env_data'] = lab_envs_data[info['lab_env']]
    else:
        info['lab_env_data'] = None

# Saving new info - in new file
with open(new_file, 'w') as file:
    yaml.safe_dump(devices_data, file, default_flow_style=False)