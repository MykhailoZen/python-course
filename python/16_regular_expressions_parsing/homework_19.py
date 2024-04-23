import re
import subprocess
import json
import pathlib
import yaml

if __name__ == '__main__':

    # 1. RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses
    # of the main network interface. It's preferred to use a single regular expression.

    res = subprocess.run('ifconfig en0'.split(), capture_output=True, encoding="utf-8")
    res = res.stdout
    print(res)

    match_ip = re.search(r'\d+\.\d+\.\d+\.\d+', res)
    print("IP address:", match_ip.group())

    match_mac = re.search(r'(ether) (\w+:\w+:\w+:\w+:\w+:\w+)', res)
    print("MAC address:", match_mac.group(2))

    # 2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, which
    # has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json, set it
    # for the corresponding device to None.

    file_json = pathlib.Path('lab_envs.json')
    text = file_json.read_text()
    data = json.loads(text)

    lab11_env_1 = data['lab11-env-1']
    lab11_env_2 = data['lab11-env-2']
    lab11_env_3 = data['lab11-env-3']

    file_yaml = pathlib.Path('devices.yaml')
    with file_yaml.open() as stream:
        data_yaml = yaml.safe_load(stream)

    data_yaml['knight-lamar']['lab_env'] = lab11_env_1
    data_yaml['goldfish-neutron']['lab_env'] = lab11_env_2
    data_yaml['hero-calcium']['lab_env'] = lab11_env_3
    data_yaml['jaws-sand']['lab_env'] = 'None'

    with pathlib.Path('devices_new_info.yaml').open('w') as write:
        yaml.safe_dump(data_yaml, write)
