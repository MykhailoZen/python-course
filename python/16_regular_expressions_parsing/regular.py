import subprocess
import re


def regex():
    # res = subprocess.run("ifconfig en0".split(), capture_output=True)
    res = subprocess.check_output(["ifconfig", "en0"]).decode("utf-8")

    pattern = r"(?P<inet>[\d.]+) (?P<ether>(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2})"

    match = re.search(pattern, res, re.MULTILINE)

    if match:
        inet = match.group(1)
        ip_address = match.group(2)
        print(f"en0: {inet}\nIP Address: {ip_address}")
    else:
        print("No network interface found.")


if __name__ == "__main__":
    regex()
