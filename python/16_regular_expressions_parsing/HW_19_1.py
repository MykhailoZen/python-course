# 1. RegExp: write a script that parses "ifconfig" output
# using the "re" module and prints the MAC & IP addresses
# of the main network interface. It's preferred to use a
# single regular expression.

import re
import subprocess

res = subprocess.run("ifconfig", capture_output=True)
output = res.stdout.decode()

pattern = r"""
    en0.*?            # A string containing "en0" and any characters up to the next occurrences
    (?:ether\s+)      # Non-capturing group to match "ether" followed by whitespace
    ([\da-fA-F:]+)    # Capture group for MAC address
    .*?               # Any characters
    (?:inet\s+)       # Non-capturing group to match "inet" followed by whitespace
    ([\d.]+)         # Capture group for IPv4 address
"""

matches = re.findall(pattern, output, re.DOTALL | re.VERBOSE)

if __name__ == "__main__":
    if matches:
        mac_address, ip_address = matches[0]
        print(f"MAC address: {mac_address}")
        print(f"IP address: {ip_address}")
    else:
        print("MAC and IP addresses not found.")
