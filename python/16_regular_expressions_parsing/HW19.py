import re
import subprocess
import json
import yaml


# 1. RegExp: write a script that parses "ifconfig" output using the "re" module
# and prints the MAC & IP addresses of the main network interface.
# It's preferred to use a single regular expression.


cmd_ifconfig = subprocess.Popen(
    ['ifconfig'], stdout=subprocess.PIPE, text=True
)
cmd_grep_en0 = subprocess.Popen(
    ['grep', "-A", "5", 'en0'], stdin=cmd_ifconfig.stdout, stdout=subprocess.PIPE, text=True
)

output, _ = cmd_grep_en0.communicate()

print(f'Output of ifconfig is: \n{output}')

pattern_mac = r'ether ([0-9a-fA-F:]+)'
pattern_ip = r'inet ([0-9.]+)'

match_mac = re.search(pattern_mac, output)
match_ip = re.search(pattern_ip, output)

print(match_mac, match_ip)

if match_mac:
    mac_address = match_mac.group(1)
    print(f"MAC Address is {mac_address}")
else:
    raise EnvironmentError('MAC Address is not found. Something went wrong')

if match_ip:
    ip_address = match_ip.group(1)
    print(f'IP Address is {ip_address}')
else:
    raise EnvironmentError('IP Address is not found. Something went wrong')


# 2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file,
# which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json,
# set it for the corresponding device to None.

def load_yaml(y_file):
    with open(y_file, 'r') as file:
        return yaml.safe_load(file)


def load_json(j_file):
    with open(j_file, 'r') as file:
        return json.load(file)


def unite_files(file_devices, file_env, file_output):
    info_devices = load_yaml(file_devices)
    info_env = load_json(file_env)

    dict_lab_env = {env: values for env, values in info_env.items()}
    print(dict_lab_env)

    for device_name, device_details in info_devices.items():
        lab_env = device_details.get('lab_env', None)
        if lab_env in dict_lab_env:
            info_devices[device_name]['lab_env'] = dict_lab_env[lab_env]
        else:
            info_devices[device_name]['lab_env'] = None

    with open(file_output, 'w') as file:
        yaml.dump(info_devices, file)


if __name__ == '__main__':
    file_devices = 'devices.yaml'
    file_env = 'lab_envs.json'
    file_output = 'parse_result.yaml'
    unite_files(file_devices, file_env, file_output)

