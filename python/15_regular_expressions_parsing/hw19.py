
import re
import json
import yaml

#1.RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses of the main network interface.

pattern = r'en0:.*?ether\s+([0-9a-fA-F:]+).*?inet\s+([0-9.]+)\s+'

ifconfig = """
    lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
         options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
         inet 127.0.0.1 netmask 0xff000000 
         inet6 ::1 prefixlen 128 
         inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
         nd6 options=201<PERFORMNUD,DAD>
    gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
    stf0: flags=0<> mtu 1280
    en10: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
         ether ac:de:48:00:11:22 
         inet6 fe80::aede:48ff:fe00:1122%en10 prefixlen 64 scopeid 0x4 
         nd6 options=201<PERFORMNUD,DAD>
         media: autoselect (100baseTX <full-duplex>)
         status: active
    ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
         options=400<CHANNEL_IO>
         ether 36:7d:da:7d:72:55 
         media: autoselect
         status: inactive
    en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
         options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
         ether 14:7d:da:7d:72:55 
         inet6 fe80::10:e65f:50df:2184%en0 prefixlen 64 secured scopeid 0x6 
         inet 192.168.50.169 netmask 0xffffff00 broadcast 192.168.50.255
         nd6 options=201<PERFORMNUD,DAD>
         media: autoselect
         status: active
    awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
         options=400<CHANNEL_IO>
         ether 3e:81:8d:b0:74:0d 
         inet6 fe80::3c81:8dff:feb0:740d%awdl0 prefixlen 64 scopeid 0x7 
         nd6 options=201<PERFORMNUD,DAD>
         media: autoselect
         status: active
"""

match = re.search(pattern, ifconfig, re.DOTALL)
mac_address = match.group(1)
ip_address = match.group(2)
print("MAC:", mac_address)
print("IP:", ip_address)


#2.JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json, set it for the corresponding device to None.

combined_dict = {}

with open("hw19_devices.yaml", "r") as devices_file:
    devices = yaml.safe_load(devices_file)

with open("hw19_lab_envs.json", "r") as lab_envs_file:
    lab_envs = json.load(lab_envs_file)

for device, info in devices.items():
    lab_env = info.get("lab_env")
    if lab_env in lab_envs:
        info["lab_env_info"] = lab_envs[lab_env]
    else:
        info["lab_env_info"] = None
    combined_dict[device] = info

with open("combined_file.yaml", "w") as combined_file:
    yaml.dump(combined_dict, combined_file)