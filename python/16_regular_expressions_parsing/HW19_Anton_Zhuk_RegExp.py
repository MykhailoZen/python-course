import re
import subprocess


def regular_expressions_parsing():
    ifconfig_output = subprocess.check_output(["ifconfig"]).decode("utf-8")

    pattern = r"en0:\s.*?ether\s([0-9a-fA-F:]+).*?inet\s(\d+\.\d+\.\d+\.\d+)"

    matches = re.findall(pattern, ifconfig_output, re.DOTALL)

    if matches:
        print("MAC Address:", matches[0][0])
        print("IP Address:", matches[0][1])
    else:
        print(f"No network interface found.")


regular_expressions_parsing()
