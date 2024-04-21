import re
import subprocess
import json
import yaml

"""
1. RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses of 
the main network interface. It's preferred to use a single regular expression.
"""


def get_network_info():
    try:
        # Run ifconfig command and capture its output
        output = subprocess.check_output(["/sbin/ifconfig"]).decode("utf-8")

        # Define regular expression pattern to match MAC and IP addresses
        pattern = r"([0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){5})|inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

        # Search for matches in the output
        matches = re.findall(pattern, output)

        # Extract MAC and IP addresses of the main network interface
        main_interface_mac = None
        main_interface_ip = None
        for match in matches:
            if match[0] and match[1]:
                main_interface_mac = match[0]
                main_interface_ip = match[1]
                break

        return main_interface_mac, main_interface_ip
    except subprocess.CalledProcessError as e:
        print("Error executing ifconfig:", e)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


# Get MAC and IP addresses of the main network interface
mac_address, ip_address = get_network_info()

# Print the MAC and IP addresses
if mac_address and ip_address:
    print("MAC Address:", mac_address)
    print("IP Address:", ip_address)
else:
    print("Failed to retrieve MAC and IP addresses.")


def get_network_info_1(interface='en0'):
    try:
        # Run ifconfig command for the specified interface and capture its output
        result = subprocess.run(['ifconfig', interface], capture_output=True)
        output = result.stdout.decode()

        # Define regular expression pattern to match MAC and IP addresses
        pattern = r"ether ([0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){5}).*?inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

        # Search for matches in the output
        matches = re.findall(pattern, output)

        # Extract MAC and IP addresses
        if matches:
            mac_address, ip_address = matches[0]
            return mac_address, ip_address
        else:
            return None, None
    except subprocess.CalledProcessError as e:
        print("Error executing ifconfig:", e)
        return None, None
    except Exception as e:
        print("An error occurred:", e)
        return None, None


# Get MAC and IP addresses for the 'en0' interface
mac_address, ip_address = get_network_info_1()

# Print the MAC and IP addresses
if mac_address and ip_address:
    print("MAC Address:", mac_address)
    print("IP Address:", ip_address)
else:
    print("Failed to retrieve MAC and IP addresses.")

'''
2. JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, 
which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json, set it for the
corresponding device to None.
'''

# Load devices.yaml
with open("devices.yaml", "r") as devices_yaml_file:
    devices_yaml = yaml.safe_load(devices_yaml_file)

# Load lab_envs.json
with open("lab_envs.json", "r") as lab_envs_file:
    lab_envs_json = json.load(lab_envs_file)

# Iterate through devices and fill lab_env attribute
for device_name, device_info in devices_yaml.items():
    lab_env = device_info.get("lab_env")
    if lab_env in lab_envs_json:
        device_info["lab_env"] = lab_envs_json[lab_env]
    else:
        device_info["lab_env"] = None

# Write combined YAML to a new file
with open("combined_devices.yaml", "w") as combined_file:
    yaml.dump(devices_yaml, combined_file)



