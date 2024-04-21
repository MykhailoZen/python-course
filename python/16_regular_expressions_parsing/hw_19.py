import re
import subprocess


def get_network_info():
    try:
        output = subprocess.check_output(["ifconfig"]).decode("utf-8")
        return output
    except subprocess.CalledProcessError:
        print("Error: Unable to execute ifconfig command")
        return None


def parse_network_info(ifconfig_output):
    # Define the regular expression pattern to extract MAC and IP addresses
    pattern = r"en0:.*?ether (\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}).*?inet\s(?:addr:)?(\d+\.\d+\.\d+\.\d+)"

    # Find matches for en0 interface
    match = re.search(pattern, ifconfig_output, re.DOTALL)

    if match:
        main_interface_mac = match.group(1)
        main_interface_ip = match.group(2)
    else:
        main_interface_mac = None
        main_interface_ip = None

    return main_interface_mac, main_interface_ip


if __name__ == "__main__":
    ifconfig_output = get_network_info()
    if ifconfig_output:
        main_interface_mac, main_interface_ip = parse_network_info(
            ifconfig_output
        )
        print("MAC Address:", main_interface_mac)
        print("IP Address:", main_interface_ip)
