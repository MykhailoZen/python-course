import pathlib
import subprocess
import re
import json

import yaml



#1. RegExp
if __name__ == '__main__':
    res = subprocess.run('ifconfig en0'.split(), capture_output=True)
    result = res.stdout.decode()
    print("Result from ifconfig:")
    print(result)

    matches = re.findall(r'(ether|inet)\s+(\S+)', result, re.MULTILINE)

    if matches:
        for match in matches:
            print(match[0], match[1])
    else:
        print("No matches found.")

#2. JSON & YAML
def combine_files(devices_yaml, lab_envs_json):

    with open(devices_yaml, 'r') as yaml_stream:
        devices = yaml.safe_load(yaml_stream)

    with open(lab_envs_json, 'r') as json_stream:
        lab_envs = json.load(json_stream)

    combined = {}
    for key in devices:
        device_info = devices[key]
        lab_name = device_info.get('lab_env')
        lab_info = lab_envs.get(lab_name, 'None')
        lab_env = {'name': lab_name, 'lab_info': lab_info}
        device_info['lab_env'] = lab_env
        combined[key] = device_info

    combined_data = yaml.dump(devices, default_flow_style=False)

    with open('combined_devices.yaml', 'w') as file:
        file.write(combined_data)

if __name__ == "__main__":
    yaml_file = "/Users/artem.bezvuhliak/Downloads/devices.yaml"
    json_file = "/Users/artem.bezvuhliak/Downloads/lab_envs.json"
    combine_files(yaml_file, json_file)
