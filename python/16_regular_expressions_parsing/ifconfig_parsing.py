import re
import subprocess

# Run the ifconfig en0 command and capture its output
output = subprocess.check_output(['ifconfig', 'en0'])

# Decode the output from bytes to string
output_str = output.decode('utf-8')

# Pattern to match MAC and IP addresses
pattern = r'ether\s+([0-9a-fA-F:]+).*?inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

# Find the MAC and IP addresses
match = re.search(pattern, output_str, re.MULTILINE | re.DOTALL)
if match:
    mac, ip = match.groups()
    print(f"MAC Address: {mac}")
    print(f"IP Address: {ip}")
else:
    print("MAC or IP address not found.")