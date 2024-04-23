
# 1. RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses of the
# main network interface. It's preferred to use a single regular expression.

import re
import subprocess

def ifconfig_func():
    result = subprocess.run(["ifconfig"], capture_output=True, text=True)
    output = result.stdout
    pattern = r'en0:.*?ether ((?:[0-9a-fA-F]{2}:?){5}[0-9a-fA-F]{2}).*?inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    match = re.search(pattern, output, re.DOTALL)
    if match:
        print(f"Your MAC address: {match.group(1)}")
        print(f"Your IP address: {match.group(2)}")
    else:
        print("Error")

# check func
ifconfig_func()