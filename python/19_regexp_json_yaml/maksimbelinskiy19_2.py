import json

import yaml

list_of_device = []

with open("lab_envs.json") as json_file:
    envs = json.load(json_file)

with open("devices.yaml") as stream:
    devices = yaml.safe_load(stream)

# print("Environments:", envs.items())
# print("Devices:", devices.items())

for device_name, device_info in devices.items():
    # print("Device name:", device_name)
    # print("Device info:", device_info)
    lab_env = device_info.get("lab_env")
    if lab_env in envs:
        device_info["lab_env"] = envs.get(lab_env)
    else:
        device_info["lab_env"] = None

# print("Updated devices:", devices.items())
with open("updated_devices.yaml", "w") as combined_file:
    yaml.dump(devices, combined_file)
