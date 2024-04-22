import re
import subprocess

def parse_ifconfig_output(output):
    pattern = r"ether ([\w:]+).*?inet (\d+\.\d+\.\d+\.\d+)"
    matches = re.search(pattern, output, re.DOTALL)
    if matches:
        mac_address = matches.group(1)
        ip_address = matches.group(2)
        return mac_address, ip_address
    else:
        return None, None

def main():
    output = subprocess.check_output(["ifconfig"]).decode("utf-8")
    mac_address, ip_address = parse_ifconfig_output(output)
    if mac_address and ip_address:
        print("MAC адрес:", mac_address)
        print("IP адрес:", ip_address)
    else:
        print("Не удалось найти MAC и IP адреса.")

if __name__ == "__main__":
    main()
