# given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, which has "lab_env"
# attribute filled for each device. If there is no such env in the lab_envs.json, set it for the corresponding
# device to None.

import json
import yaml

if __name__ == "__main__":

    with open("devices.yaml", "r") as devices_yaml:
        devices = yaml.safe_load(devices_yaml)
        # print(devices)

    with open("lab_envs.json", "r") as labs_json:
        labs = json.load(labs_json)
        # print(labs)

    for nodes, node_info in devices.items():
        lab_env = node_info.get("lab_env")
        # print(lab_env)

        if lab_env in labs:
            node_info["lab_env"] = labs[lab_env]
        else:
            node_info["lab_env"] = "None"

    # print(devices)
    with open("combined.yaml", "w") as combined_file:
        yaml.dump(devices, combined_file)
