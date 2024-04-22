import re
import subprocess

# Be aware that I am using wired connection and en9 is default interface for my laptop
# If your default interface differs, change it accordingly

res = subprocess.run("ifconfig en9".split(), capture_output=True)
output = res.stdout.decode()

pattern = r"(?:inet\s|ether\s)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2})"  # noqa: E501


result = re.findall(pattern, output)

print("IP address:", result[1])
print("MAC address:", result[0])
