import re
import subprocess
import yaml
import json


def get_network_info():
    result = subprocess.run(["ifconfig"], capture_output=True, text=True)
    ifconfig_output = result.stdout
    pattern = re.compile(
        r"(\w+):\s.*?inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?ether\s([0-9a-f:]{17})",
        re.S,
    )
    matches = pattern.findall(ifconfig_output)
    for interface, ip, mac in matches:
        print(f"Interface: {interface}, IP Address: {ip}, MAC Address: {mac}")

    yaml_file_path = "/Users/ivan.liko/Documents/Automation Course/python-course/python/16_regular_expressions_parsing/Ring devices.yaml"
    json_file_path = "/Users/ivan.liko/Documents/Automation Course/python-course/python/16_regular_expressions_parsing/Lab Envs.json"
    output_file_path = "/Users/ivan.liko/Documents/Automation Course/python-course/python/16_regular_expressions_parsing/Combined.yaml"
    combine_files(yaml_file_path, json_file_path, output_file_path)
    print("Files have been successfully combined into", output_file_path)


def parse_yaml_file(path):
    with open(path, "r") as file:
        data = yaml.safe_load(file)
        return data


def parse_json_file(path):
    with open(path, "r") as file:
        data = json.load(file)
        return data


def combine_files(devices_file, lab_envs_file, output_file):
    devices = parse_yaml_file(devices_file)
    lab_envs = parse_json_file(lab_envs_file)
    for device_name, device_info in devices.items():
        lab_env_data = lab_envs.get(device_info["lab_env"], None)
        if lab_env_data is not None:
            device_info["lab_env"] = {device_info["lab_env"]: lab_env_data}
        else:
            device_info["lab_env"] = "None"
    with open(output_file, "w") as file:
        yaml.dump(devices, file)


get_network_info()
