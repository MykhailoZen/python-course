import re
import subprocess

def get_main_interface_info():
    # Run the ifconfig command and capture its output
    output = subprocess.check_output(["ifconfig"]).decode("utf-8")

    # Define a regular expression pattern to match MAC and IP address
    pattern = r"en0.*?ether\s+([0-9a-fA-F:]+).*?inet\s+([0-9.]+)"

    # Search for the pattern in the ifconfig output
    match = re.search(pattern, output, re.DOTALL)

    if match:
        mac_address = match.group(1)
        ip_address = match.group(2)
        return mac_address, ip_address
    else:
        return None, None

# Get MAC and IP address of the main network interface
mac_address, ip_address = get_main_interface_info()

# the results print
if mac_address and ip_address:
    print("MAC Address:", mac_address)
    print("IP Address:", ip_address)
else:
    print("Unable to retrieve MAC and IP addresses.")
