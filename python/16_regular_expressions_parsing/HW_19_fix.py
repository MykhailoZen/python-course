import json
import re
import subprocess

import yaml

# 1. RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses of
# the main network interface. It's preferred to use a single regular expression.

# Run ifconfig and get the output
result = subprocess.run("ifconfig", capture_output=True, text=True)
output = result.stdout.strip()
'''
A part of output ifconfig:
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
ether 88:66:5a:13:f7:14
inet6 fe80::1ca5:2762:5b1b:b70%en0 prefixlen 64 secured scopeid 0x8
inet6 fd52:2549:ca89:1:c45:fcc1:8e05:3517 prefixlen 64 autoconf secured
inet 192.168.4.22 netmask 0xfffffc00 broadcast 192.168.7.255
nd6 options=201<PERFORMNUD,DAD>
media: autoselect
status: active
'''

# Use a single regular expression to find the MAC and IP addresses
pattern = r"en[0].*?ether\s+([\w:]+).*?inet\s+(\d+\.\d+\.\d+\.\d+)"
# one more regular expression to find the MAC and IP addresses
# pattern = r"en[0].*?ether\s+([\w:]+).*?inet\s+([\w.]+)"
match = re.search(pattern, output, re.DOTALL)

if match:
    mac_address = match.group(1)
    ip_address = match.group(2)
    print(f"MAC Address en0: {mac_address}")
    print(f"IP Address en0: {ip_address}")
else:
    print("MAC and IP addresses not found.")

# 2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file,
# which has "lab_env" attribute filled for each device.
# If there is no such env in the lab_envs.json, set it for the
# corresponding device to None.

#parse yaml file
with open('devices.yaml', 'r') as devices_yaml:
    devices = yaml.safe_load(devices_yaml)
#parse json file
with open('lab_envs.json', 'r') as lab_envs_json:
    lab_envs = json.load(lab_envs_json)
# #combining the files:
for device in devices.values():
    lab_env_name = device.get('lab_env')
    if lab_env_name in lab_envs:
        device['lab_env'] = lab_envs[lab_env_name]

# Write combined data to devices_vs_lab_env.yaml
with open('devices_vs_lab_env_new.yaml', 'w') as devices_vs_lab_env:
    yaml.safe_dump(devices, devices_vs_lab_env)