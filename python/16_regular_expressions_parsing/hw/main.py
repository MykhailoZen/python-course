import re
import subprocess
import yaml
import json

# Run ifconfig command and capture output
res = subprocess.run(["ifconfig"], capture_output=True, text=True)
output = res.stdout

# Define the regular expression pattern
pattern = r"(?<=inet\s)\d+\.\d+\.\d+\.\d+|(?<=ether\s)[0-9a-fA-F:]{17}"

# Search for the pattern in the output
matches = re.findall(pattern, output)

# Extract MAC and IP addresses
mac_address = matches[0]
ip_address = matches[1]

print(f"MAC Address: {mac_address}")
print(f"IP Address: {ip_address}")


# Load devices.yaml
with open("devices.yaml", "r") as f:
    devices_yaml = yaml.safe_load(f)

# Load lab_envs.json
with open("lab_envs.json", "r") as f:
    lab_envs_json = json.load(f)

# Combine devices.yaml and lab_envs.json
for device_name, device_info in devices_yaml.items():
    lab_env = device_info.get("lab_env")
    if lab_env in lab_envs_json:
        device_info["lab_env"] = lab_envs_json[lab_env]
    else:
        device_info["lab_env"] = None

# Write combined YAML to a new file
with open("combined_devices.yaml", "w") as combined_file:
    yaml.dump(devices_yaml, combined_file)

print("Combined YAML file created successfully!")
