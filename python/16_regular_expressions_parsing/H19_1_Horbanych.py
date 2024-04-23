#1. RegExp: write a script that parses "ifconfig" output using the "re" module and prints
# the MAC & IP addresses of the main network interface.
# It's preferred to use a single regular expression.

import subprocess
import re


# Run ifconfig command and capture the output
output = subprocess.check_output(['ifconfig']).decode()

# Regular expression to match MAC and IP addresses
regex = r'inet addr:(\d+\.\d+\.\d+\.\d+).*?HWaddr\s([0-9a-fA-F:]{17})'

# All matches
matches = re.findall(regex, output)

# Print MAC and IP addres
if matches:
    mac_address, ip_address = matches[0]
    print(f"MAC Address: {mac_address}")
    print(f"IP Address: {ip_address}")
else:
    print("No MAC and IP addresses found.")




