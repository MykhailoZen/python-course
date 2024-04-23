import yaml
import json


# Load devices YAML file
with open('devices.yaml', 'r') as devices_file:
    devices_data = yaml.safe_load(devices_file)

    # Load lab environments JSON file
with open('lab_envs.json', 'r') as lab_envs_file:
    lab_envs_data = json.load(lab_envs_file)

    # Combine data
combined_data = []
for device in devices_data:
    device_name = device['device_name']
    # Check if lab environment exists for the device
    if device_name in lab_envs_data:
            lab_env = lab_envs_data[device_name]
    else:
        lab_env = None
    device['lab_env'] = lab_env
    combined_data.append(device)

    # Write combined data to output YAML file
with open('output.yaml', 'w') as output_file:
    yaml.dump(combined_data, output_file)



