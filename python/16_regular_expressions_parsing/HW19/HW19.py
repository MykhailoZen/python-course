import re
import subprocess


def get_network_info():
    # Run ifconfig
    result = subprocess.run(["ifconfig"], capture_output=True, text=True)
    ifconfig_output = result.stdout

    # Define regular expression pattern
    pattern = r"inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?ether ([0-9a-fA-F:]{17})"

    # Use re.findall to find all matches of the pattern in ifconfig output
    matches = re.findall(pattern, ifconfig_output, re.DOTALL)

    if matches:
        return matches[0]
    else:
        return None, None


# Get MAC and IP addresses of the main network interface
mac_address, ip_address = get_network_info()

# Print the MAC and IP addresses
if mac_address and ip_address:
    print("MAC Address:", mac_address)
    print("IP Address:", ip_address)
else:
    print("NO MAC ADDRESS FOUND")
