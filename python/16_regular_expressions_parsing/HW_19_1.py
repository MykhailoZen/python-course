# 1. RegExp: write a script that parses "ifconfig" output
# using the "re" module and prints the MAC & IP addresses
# of the main network interface. It's preferred to use a
# single regular expression.

import re
import subprocess

res = subprocess.run("ifconfig en0".split(), capture_output=True)
output = res.stdout.decode()

# Option 1 with two separate patterns for IP and MAC
ip_pattern = r"(?:inet\s)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
mac_pattern = (
    r"(?:ether\s)([\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2})"
)
combine_pattern = rf"{ip_pattern}|{mac_pattern}"

matches_1 = re.findall(combine_pattern, output)

# Option 2 with one common pattern for IP and MAC
pattern = r"""
    (?:inet\s|ether\s)      # Non-capturing group to match "inet" or "ether" followed by a space
    (                       # Start of capturing group
    \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}     # IPv4 address mapping in the format "xxx.xxx.xxx.xxx"
    |                       # Or
    [\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2} # MAC address mapping in the format "xx:xx:xx:xx:xx:xx"
    )                       # End of capturing group
"""

matches_2 = re.findall(pattern, output, re.VERBOSE)


if __name__ == "__main__":
    print("Option 1 with two separate patterns for IP and MAC")
    if matches_1:
        for match in matches_1:
            ip_addres, mac_address = match
            if ip_addres:
                print(f"IP address {ip_addres}")
            if mac_address:
                print(f"MAC address {mac_address}")

    print("Option 2 with one common pattern for IP and MAC")
    if matches_2:
        for match in matches_2:
            print(match)
