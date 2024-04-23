import json
import pathlib
import yaml


def create_combined_data(yaml_info, json_info):
    combined_data = {}
    for device_name, device_info in yaml_info.items():
        combined_info = device_info.copy()
        if device_info['lab_env'] in json_info:
            environment = device_info['lab_env']
            combined_info['lab_env'] = json_info[environment]
        else:
            combined_info['lab_env'] = None
        combined_data[device_name] = combined_info
    return combined_data


if __name__ == "__main__":
    json_file = pathlib.Path('./lab_envs.json')
    text = json_file.read_text()
    json_data = json.loads(text)

    yaml_file = pathlib.Path('./devices.yaml')
    with yaml_file.open() as stream:
        yaml_data = yaml.safe_load(stream)

    with open('combined.yaml', 'w') as file:
        yaml.dump(create_combined_data(yaml_data, json_data), file)
