"""
HOMEWORK 19
1. RegExp: write a script that parses "ifconfig" output using the "re" module and prints the MAC & IP addresses of the main network interface. It's preferred to use a single regular expression.
"""

"""
import re

def parse_ifconfig(ifconfig_file):
    with open(ifconfig_file, 'r') as f:
        output = f.read()

    # Define the regular expression pattern
    pattern = r'en0:.*?ether ((?:[0-9a-fA-F]{2}:?){5}[0-9a-fA-F]{2}).*?inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    # Search for the pattern in the output
    match = re.search(pattern, output, re.DOTALL)

    # If a match is found, print the results
    if match:
        print("MAC (ether) Address:", match.group(1))
        print("IP (inet) Address:", match.group(2))
    else:
        print("No match found")

# Call the function with the path to the ifconfig file
parse_ifconfig("ifconfig.txt")

"""

import re
import subprocess

def parse_ifconfig():
    # Run the ifconfig command and get the output
    result = subprocess.run(["ifconfig"], capture_output=True, text=True)
    output = result.stdout

    # Define the regular expression pattern
    pattern = r'en0:.*?ether ((?:[0-9a-fA-F]{2}:?){5}[0-9a-fA-F]{2}).*?inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    # Search for the pattern in the output
    match = re.search(pattern, output, re.DOTALL)

    # If a match is found, print the results
    if match:
        print("MAC (ether) Address:", match.group(1))
        print("IP (inet) Address:", match.group(2))
    else:
        print("No match found")

# Call the function to parse ifconfig output
parse_ifconfig()

