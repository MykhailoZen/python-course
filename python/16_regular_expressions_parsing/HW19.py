import re
import subprocess

output = subprocess.check_output(["ifconfig", "en0"]).decode("utf-8")
print(output)
pattern = r'ether [a-zA-Z\d:]+|inet [\d.]+'
matches = re.findall(pattern, output)


for match in matches:
    match_split = match.split(" ")
    address = match_split[1]
    if "ether" in match:
        print(f"MAC Address: {address}")
    elif "inet" in match:
        print(f"IP Address: {address}")

