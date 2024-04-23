"""
HOMEWORK 19
2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json, set it for the corresponding device to None
"""

import yaml
import json

# Load devices.yaml
with open('devices.yml', 'r') as f:
    devices = yaml.safe_load(f)

# Load lab_envs.json
with open('lab_envs.json', 'r') as f:
    lab_envs = json.load(f)

# Combine data and set lab_env attribute
for device_name, device_info in devices.items():
    lab_env = lab_envs.get(device_info['lab_env'], None)
    device_info['lab_env'] = lab_env

# Write combined data to combined.yaml
with open('combined.yaml', 'w') as f:
    yaml.dump(devices, f, default_flow_style=False)
