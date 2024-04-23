import subprocess
import re

# Run ifconfig and capture its output
proc1 = subprocess.check_output("ifconfig").decode("utf-8")



proc = """en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
        ether 14:7d:da:19:97:1b 
        inet6 fe80::7f:e74b:3908:45f7%en0 prefixlen 64 secured scopeid 0x6 
        inet 192.168.88.40 netmask 0xffffff00 broadcast 192.168.88.255
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect
        status: active"""




# Define the regular expression pattern to match en0 interface
pattern1 = r'\s+\bether\s(\b\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}\b)'
pattern2 = r'\s+\binet\s(\b\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\b)'

# Search for the pattern in the ifconfig output
result1 = re.search(pattern1, proc)
result2 = re.search(pattern2, proc)

# Check if a match is found
if result1:
    # Print the information related to the en0 interface
    mac = (result1.group(1))
    print(f"MAC: %s" % mac)
else:
    print("en0 interface information not found.")

if result2:
    # Print the information related to the en0 interface
    ip = (result2.group(1))
    print(f"ip: %s" % ip)
else:
    print("en0 interface information not found.")