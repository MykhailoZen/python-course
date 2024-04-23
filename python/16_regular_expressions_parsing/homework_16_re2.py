import json
import yaml

def combine_device_info():
    # reading JSON
    with open('lab_envs.json', 'r') as json_file:
        lab_envs = json.load(json_file)

    # reading YAML
    with open('devices.yaml', 'r') as yaml_file:
        devices = yaml.safe_load(yaml_file)

    # updating info
    updated_devices = {}
    for device_id, details in devices.items():
        # get lab_env for each device
        lab_env = details['lab_env']
        env_info = lab_envs.get(lab_env, None)

        # device info updating
        updated_devices[device_id] = details
        updated_devices[device_id]['env_info'] = env_info

    # writing data to new YAML file
    with open('combined_devices.yaml', 'w') as output_file:
        yaml.dump(updated_devices, output_file, default_flow_style=False)


combine_device_info()
