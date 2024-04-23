import re
import subprocess
import json
import yaml
"""
1. RegExp: write a script that parses "ifconfig" output using the "re" module and 
prints the MAC & IP addresses of the main network interface. 
It's preferred to use a single regular expression.
"""
ifconfig = str(subprocess.run('ifconfig en0'.split(), capture_output=True))
print([re.search(_, ifconfig) for _ in [r'(\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2})',
                                                    '(\d{3}\.\d{3}.\d{1,3}.\d{1,3})']])

"""
2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them 
into one YAML file, which has "lab_env" attribute filled for each device. 
If there is no such env in the lab_envs.json, set it for the corresponding device to None.
"""

with open("devices.yaml", "r") as devices_yaml_file:
    devices_yaml = yaml.safe_load(devices_yaml_file)
print(devices_yaml)

with open("lab_envs.json", "r") as lab_envs_file:
    lab_envs_json = json.load(lab_envs_file)
print(lab_envs_json)

for device, attribute in devices_yaml.items():
    lab_env = attribute.get("lab_env")
    if lab_env in lab_envs_json:
        attribute["lab_env"] = lab_envs_json[lab_env]
    else:
        attribute["lab_env"] = None

with open("Combined.yaml", "w") as combined:
    yaml.dump(devices_yaml, combined)
