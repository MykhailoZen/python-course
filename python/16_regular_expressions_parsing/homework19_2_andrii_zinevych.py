import yaml
import json

# Load data from devices.yaml
with open('devices.yaml', 'r') as f:
    devices_yaml = yaml.safe_load(f)

# Load data from lab_envs.json
with open('lab_envs.json', 'r') as f:
    lab_envs_json = json.load(f)

# Create a list to store combined data
combined_data = []

# Initialize counter for matched lab_envs
matched_count = 0

# Update combined data with devices from devices.yaml
for device_name, device_info in devices_yaml.items():
    lab_env_name = device_info.get('lab_env')
    lab_env_info = lab_envs_json.get(lab_env_name)
    lab_env_value = lab_env_info if lab_env_info else 'not matched'
    combined_data.append({
        'device_name': device_name,
        'device_type': device_info.get('device_type'),
        'lab_env': lab_env_name,
        'lab_env_value': lab_env_value
    })
    if lab_env_info:
        matched_count += 1

# Write combined data to combined.yaml
with open('combined.yaml', 'w') as f:
    for data in combined_data:
        f.write(yaml.dump(data))
        f.write('------------------\n')  # Separator line

# Write count of matched lab_envs to separate YAML file
with open('matched_lab_envs.yaml', 'w') as f:
    yaml.dump({'matched_lab_envs': matched_count}, f)

print("Combined YAML file has been created.")
print(f"Number of matched lab_envs: {matched_count}")
