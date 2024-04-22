import json
import pathlib
import re
import subprocess

import yaml

#  RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses
#  of the main network interface. It's preferred to use a single regular expression. RegExp: write a script that parses
#  "ifconfig" output using the "re" module and prints the MAC & IP addresses of the main network interface.
#  It's preferred to use a single regular expression.

result = subprocess.run("ifconfig en0".split(), capture_output=True)
output = result.stdout.decode()

pattern = r"en0.*?ether\s*(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}).*?inet\s*((\d{1,3}\.){3}\d{1,3})"

matches = re.search(pattern, output, re.DOTALL)
if matches:
    mac_address = matches.group(1)
    ip_address = matches.group(3)
    print("MAC Address:", mac_address)
    print("IP Address:", ip_address)
else:
    print("No MAC or IP address found for the main network interface.")

# JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file,
#  which has "lab_env" attribute filled for each device.
#  If there is no such env in the lab_envs.json, set it for the corresponding device to None.


def load_yaml(file_path):
    with file_path.open() as stream_dev:
        data = yaml.safe_load(stream_dev)
        return data


def load_json(file_path):
    with open(file_path, 'r') as lab_envs_file:
        lab_envs_json = lab_envs_file.read()
        return lab_envs_json


def merge_devices_and_envs(devices_yaml, lab_envs_json):
    merged_devices = []
    lab_envs = json.loads(lab_envs_json)
    for device_name, device_info in devices_yaml.items():
        lab_env = lab_envs.get(device_info['lab_env'], None)
        device_info['lab_env'] = lab_env if lab_env is not None else None
        merged_devices.append({device_name: device_info})
    return merged_devices


def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump_all(data, file)


if __name__ == '__main__':
    devices_yaml_path = pathlib.Path('devices.yaml')
    lab_envs_json_path = pathlib.Path('lab_envs.json')

    # Load YAML data
    devices_data = load_yaml(devices_yaml_path)

    # Load JSON data
    env_data = load_json(lab_envs_json_path)

    # Merge devices and environments
    merged_devices = merge_devices_and_envs(devices_data, env_data)
    print(f"New combine file from {devices_yaml_path} and {lab_envs_json_path}\n {merged_devices}")

    # Write merged data to YAML file
    write_yaml(merged_devices, 'combined_devices.yaml')
