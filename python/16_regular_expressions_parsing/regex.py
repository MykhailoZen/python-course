import subprocess
import re


def get_interface_info():
    try:
        output = subprocess.check_output(["ifconfig", "en0"])
        output = output.decode("utf-8")
        ip_and_mac_pattern = (
            r"ether\s+([0-9a-fA-F:]+).*?inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}"
            r"\.\d{1,3})"
        )
        result = re.search(
            ip_and_mac_pattern, output, re.IGNORECASE | re.MULTILINE |
            re.DOTALL)
        if result:
            mac = result.group(1)
            ip = result.group(2)
            return mac, ip
        else:
            return None, None
    except subprocess.CalledProcessError:
        print("Error: Unable to run ifconfig command.")
        return None, None


if __name__ == "__main__":
    mac_address, ip_address = get_interface_info()
    if mac_address and ip_address:
        print("MAC Address:", mac_address)
        print("IP Address:", ip_address)
    else:
        print("No information available for interface")
