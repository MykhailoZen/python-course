import re
import subprocess


def get_network_info():

    output = subprocess.check_output(['ifconfig', 'en0']).decode("utf-8")
    # print(output)
    # Defining regex pattern
    pattern = r"ether ([0-9a-fA-F:]{17}).*inet (\d+\.\d+\.\d+\.\d+)"

    # searching for the pattern in the output
    match = re.search(pattern, output, re.DOTALL)

    # matching groups
    mac_address = match.group(1)
    ip_address = match.group(2)

    return ip_address, mac_address


if __name__ == "__main__":

    ip, mac = get_network_info()
    print(f"IP Address: {ip}")
    print(f"MAC Address: {mac}")


