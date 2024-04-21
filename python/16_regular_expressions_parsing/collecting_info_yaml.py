import json
import yaml

# Path to files
devices_yaml_path = 'devices.yaml'
envs_json_path = 'lab_envs.json'
output_yaml_path = 'updated_devices.yaml'

# Reading info from YAML file
with open(devices_yaml_path, 'r') as file:
    devices_data = yaml.safe_load(file)

# Reading info from JSON file
with open(envs_json_path, 'r') as file:
    lab_envs_data = json.load(file)

# Updating info, based on `lab_env` parts
for device, info in devices_data.items():
    if info['lab_env'] in lab_envs_data:
        info['lab_env_data'] = lab_envs_data[info['lab_env']]
    else:
        info['lab_env_data'] = None

# Saving info into new YAML file
with open(output_yaml_path, 'w') as file:
    yaml.safe_dump(devices_data, file, default_flow_style=False)
