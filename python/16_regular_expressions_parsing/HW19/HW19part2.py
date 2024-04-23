import json
import os

import yaml

# Make sure that the files are present in script folder
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load devices.yaml
devices_yaml_path = os.path.join(current_dir, "devices.yaml")
with open(devices_yaml_path, "r") as devices_file:
    devices_data = yaml.safe_load(devices_file)

# Load lab_envs.json
lab_envs_json_path = os.path.join(current_dir, "lab_envs.json")
with open(lab_envs_json_path, "r") as lab_envs_file:
    lab_envs_data = json.load(lab_envs_file)

# Combine data and fill lab_env attribute for each device
for device_name, device_info in devices_data.items():
    lab_env = device_info.get("lab_env")
    if lab_env in lab_envs_data:
        device_info["lab_env"] = lab_envs_data[lab_env]
    else:
        device_info["lab_env"] = None

# Write combined data to a new YAML file
combined_yaml_path = os.path.join(current_dir, "combined_devices.yaml")
with open(combined_yaml_path, "w") as combined_file:
    yaml.dump(devices_data, combined_file, default_flow_style=False)

print("Done.")
