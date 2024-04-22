import re
import subprocess

# Run ifconfig command and capture its output
ifconfig_output = subprocess.run(['ifconfig'], capture_output=True, text=True).stdout

# Define regular expression pattern to match MAC and IP addresses
pattern = r'(?<=ether )([0-9a-f]{2}(?::[0-9a-f]{2}){5})|(?<=inet )(\d+\.\d+\.\d+\.\d+)'

# Find all matches in the ifconfig output
matches = re.findall(pattern, ifconfig_output)

# Print MAC and IP addresses of the main network interface
for mac, ip in matches:
    if mac:
        print(f"MAC address: {mac}")
    elif ip:
        print(f"IP address: {ip}")
