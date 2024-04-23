
#2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, which has
# "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json, set it for the corresponding
# device to None.


import yaml
import json

with open("devices.yaml", "r") as devices_f:
    data_devices = yaml.safe_load(devices_f)

with open("lab_envs.json", "r") as lab_envs_f:
    data_lab_envs = json.load(lab_envs_f)

#parce files which has "lab_env" attribute of device
for device_name, device_info in data_devices.items():
    lab_env = device_info.get("lab_env")
    if lab_env in data_lab_envs:
        device_info["lab_env"] = data_lab_envs[lab_env]
    else:
        device_info["lab_env"] = "None"

#create/write in file a parced info
with open("combined_file.yaml", "w") as combined_f:
    yaml.dump(data_devices, combined_f)