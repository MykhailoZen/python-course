import json
import yaml


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def combine_devices(devices_yaml, lab_envs_json):
    devices = load_yaml(devices_yaml)
    lab_envs = load_json(lab_envs_json)

    combined_data = {}
    for device_name, device_info in devices.items():
        lab_env = device_info['lab_env']
        if lab_env in lab_envs:
            device_info.update(lab_envs[lab_env])
        else:
            device_info['lab_env'] = 'None'
        combined_data[device_name] = device_info

    with open('combined_data.yaml', 'w') as file:
        for device_name, device_info in combined_data.items():
            yaml.dump({device_name: device_info}, file)
            file.write("\n")


combine_devices('devices.yaml', 'lab_envs.json')
