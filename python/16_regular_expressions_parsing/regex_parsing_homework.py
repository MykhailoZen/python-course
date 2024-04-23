import re
import subprocess

ifconfig_process = subprocess.run('ifconfig en0'.split(), capture_output=True)
output = ifconfig_process.stdout.decode()
print(f'Ifconfig en0 output: \n{output}')

pattern = r'inet \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|ether \w+:\w+:\w+:\w+:\w+:\w+'
result = re.findall(pattern, output)
print(f'RegEx result: ')
for i in result:
    print(i)


