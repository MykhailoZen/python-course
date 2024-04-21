import json

import yaml


# Load devices.yaml
with open("devices.yaml", "r") as devices_file:
    devices = yaml.safe_load(devices_file)

# Load lab_envs.json
with open("lab_envs.json", "r") as lab_envs_file:
    lab_envs = json.load(lab_envs_file)

# Combine information and create new YAML structure
combined_data = {}
for device, info in devices.items():
    lab_env = info.get("lab_env")
    if lab_env in lab_envs:
        info["lab_env_info"] = lab_envs[lab_env]
    else:
        info["lab_env_info"] = None
    combined_data[device] = info

# Write combined data to a new YAML file
with open("combined_devices.yaml", "w") as combined_file:
    yaml.dump(combined_data, combined_file, default_flow_style=False)
