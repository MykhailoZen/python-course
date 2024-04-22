import yaml
import json

with open("devices.yaml", "r") as devices_file:
    data_devices = yaml.safe_load(devices_file)

with open("lab_envs.json", "r") as lab_envs_file:
    data_lab_envs = json.load(lab_envs_file)

for device_name, device_info in data_devices.items():
    lab_env = device_info.get("lab_env")
    if lab_env in data_lab_envs:
        device_info["lab_env"] = data_lab_envs[lab_env]
    else:
        device_info["lab_env"] = "None"

with open("lab_devices_envs.yaml", "w") as combined_file:
    yaml.dump(data_devices, combined_file)
