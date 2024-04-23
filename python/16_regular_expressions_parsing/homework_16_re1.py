import re
import subprocess


def extract_ip_and_mac():
    # ifconfig
    result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')

    # regex
    pattern = re.compile(r'en0.*?ether\s+(\S+).*?inet\s+(\S+)', re.S)

    # match search
    match = pattern.search(output)

    if match:
        mac_address, ip_address = match.groups()
        print(f"Interface: en0, IP: {ip_address}, MAC: {mac_address}")
    else:
        print("Interface en0 not found.")


# run match function
extract_ip_and_mac()
