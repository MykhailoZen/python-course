# 1. RegExp: write a script that parses "ifconfig" output using the "re" module and prints
# the MAC & IP addresses of the main network interface. It's preferred to use a single regular expression.
import re
import subprocess


def main():
    result = subprocess.run("ifconfig en0".split(), capture_output=True)
    output = result.stdout.decode()
    print(output)

    mac_pattern = r"ether\s+([0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){5})"

    ip_pattern = r"inet\s+(\d+\.\d+\.\d+\.\d+)"

    mac_match = re.search(mac_pattern, output)
    ip_match = re.search(ip_pattern, output)

    if mac_match:
        print("MAC адреса:", mac_match.group(1))
    else:
        print("MAC адреса не знайдена")

    if ip_match:
        print("IP адреса:", ip_match.group(1))
    else:
        print("IP адреса не знайдена")


if __name__ == "__main__":
    main()

# 2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file,
# which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json,
# set it for the corresponding device to None.
import json

import yaml


def combine_envs(devices_yaml, lab_envs_json, combo_yaml):
    with open(devices_yaml, "r") as f:
        devices_data = yaml.safe_load(f)

    with open(lab_envs_json, "r") as f:
        lab_envs_data = json.load(f)

    for device, details in devices_data.items():
        lab_env = lab_envs_data.get(details.get("lab_env"))
        details["lab_env"] = lab_env if lab_env is not None else None

    with open(combo_yaml, "w") as f:
        yaml.dump(devices_data, f)


combine_envs("devices.yaml", "lab_envs.json", "combo_devices.yaml")
