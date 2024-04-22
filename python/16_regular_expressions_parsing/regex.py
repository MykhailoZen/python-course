import re
import subprocess


def parse_ipconfig_output(output):
    pattern = (r"IPv4 Address[^\n]*: ([\d.]+).*?"
               r"Physical Address[^\n]*: ([\dA-Z-]+)")
    matches = re.findall(pattern, output, re.IGNORECASE | re.DOTALL)

    for ip_address, mac_address in matches:
        return ip_address, mac_address

    return None, None


ipconfig_output = subprocess.check_output(["ipconfig", "/all"]).decode("cp1252")

ip_address, mac_address = parse_ipconfig_output(ipconfig_output)

if ip_address and mac_address:
    print("IP Address:", ip_address)
    print("MAC Address:", mac_address)
else:
    print("No IP/MAC addresses found")
