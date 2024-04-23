# 1. RegExp: write a script that parses "ifconfig" output using the "re" module and
# prints the MAC & IP addresses of the main network interface. It's preferred to use a single regular expression.

import re
import json
import yaml

ifconfig_output = """
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether a4:83:e7:0f:36:8e
	inet6 fe80::c0a:dcfd:571:5e19%en0 prefixlen 64 secured scopeid 0x6
	inet 192.168.0.142 netmask 0xffffff00 broadcast 192.168.0.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
"""

pattern = r'((?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}).*inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

matches = re.search(pattern, ifconfig_output, flags=re.DOTALL)

print(f'MAC ID: ', matches.group(1))
print(f'IP addresses: ', matches.group(2))

# 2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file,
# which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json,
# set it for the corresponding device to None.


with open('devices.yaml', 'r') as devices:
    devices_data = yaml.safe_load(devices)

with open('lab_envs.json', 'r') as lab_envs:
    lab_env_data = json.load(lab_envs)

for key, device_data in devices_data.items():
    lab_env = device_data.get('lab_env')
    if lab_env in lab_env_data:
        device_data['lab_env'] = lab_env_data[lab_env]
    else:
        device_data['lab_env'] = None

with open('combined.yaml', 'w') as combined:
    yaml.dump(devices_data, combined)

