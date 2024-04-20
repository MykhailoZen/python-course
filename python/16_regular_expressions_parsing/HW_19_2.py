# 2. JSON & YAML: given two files, devices.yaml & lab_envs.json,
# parse and combine them into one YAML file, which has "lab_env"
# attribute filled for each device. If there is no such env in
# the lab_envs.json, set it for the corresponding device to None.

import json
import os

import yaml

# Get the path to the current script directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Read information from devices.yaml
devices_file_path = os.path.join(dir_path, "devices.yml")
with open(devices_file_path, "r") as devices_file:
    devices = yaml.safe_load(devices_file)

# Read information from lab_envs.json
lab_envs_file_path = os.path.join(dir_path, "lab_envs.json")
with open(lab_envs_file_path, "r") as lab_envs_file:
    lab_envs = json.load(lab_envs_file)

# Combine information about devices with information about laboratory environments
for device_name, device_info in devices.items():
    lab_env = device_info.get("lab_env")
    if lab_env in lab_envs:
        device_info["lab_env"] = lab_envs.get(lab_env, None)
    else:
        device_info["lab_env"] = None

# Write the combined information to a new YAML file
output_file_path = os.path.join(dir_path, "combined_devices.yml")
with open(output_file_path, "w") as combined_file:
    yaml.dump(devices, combined_file, default_flow_style=False)
