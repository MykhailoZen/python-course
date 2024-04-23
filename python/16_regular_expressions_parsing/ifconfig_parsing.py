import re
import subprocess


def get_main_interface_info():
    # Run the ifconfig command and capture its output
    output = subprocess.check_output(["ifconfig", "en0"]).decode("utf-8")

    # Define the regular expression pattern to match MAC and IP addresses
    pattern = r"(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})|(inet (\d{1,3}\.){3}\d{1,3})"

    # Find all matches of the pattern in the output
    matches = re.findall(pattern, output)

    # Get the MAC and IP addresses of the main network interface
    main_interface_mac = None
    main_interface_ip = None
    for match in matches:
        if match[0]:  # MAC address match
            main_interface_mac = match[0]
        elif match[2]:  # IP address match
            main_interface_ip = match[2].split(" ")[1]

    return main_interface_mac, main_interface_ip


# Get MAC and IP addresses of the main network interface
main_interface_mac, main_interface_ip = get_main_interface_info()

# Print the MAC and IP addresses
print("MAC Address:", main_interface_mac)
print("IP Address:", main_interface_ip)
