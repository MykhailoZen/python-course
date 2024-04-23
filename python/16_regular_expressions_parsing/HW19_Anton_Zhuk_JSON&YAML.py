import yaml
import json


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def combine_files(yaml_file, json_file):
    devices = load_yaml(yaml_file)
    lab_envs = load_json(json_file)

    for device_name, device_info in devices.items():
        lab_env = device_info.get("lab_env")
        if lab_env in lab_envs:
            device_info["lab_env"] = lab_envs.get(lab_env, None)
        else:
            device_info["lab_env"] = None

    return devices


def save_combined_yaml(data, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(data, file)


if __name__ == "__main__":
    yaml_file_path = "devices.yaml"
    json_file_path = "lab_envs.json"
    output_file_path = "combined_devices.yaml"

    combined_data = combine_files(yaml_file_path, json_file_path)
    save_combined_yaml(combined_data, output_file_path)
