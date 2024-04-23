import yaml
import json
import pathlib

def merge_files(devices_file, labs_file, output_file):
    # Load devices YAML
    with open(devices_file, 'r') as f:
        devices_data = yaml.safe_load(f)

    # Load labs JSON
    with open(labs_file, 'r') as f:
        labs_data = json.load(f)

    # Process devices data and update lab_env based on labs_data
    for device, info in devices_data.items():
        lab_env_key = info.get('lab_env')
        if lab_env_key:
            lab_env_info = labs_data.get(lab_env_key, {})
            info['lab_env'] = lab_env_info
        else:
            info['lab_env'] = {}

    # Write the combined data to a new YAML file
    with open(output_file, 'w') as f:
        # Iterate over devices_data and manually format YAML output
        for device, info in devices_data.items():
            f.write(f"{device}:\n")
            f.write(f"  device_type: {info['device_type']}\n")
            f.write("  lab_env:\n")
            if info['lab_env']:
                for key, value in info['lab_env'].items():
                    f.write(f"    {key}: {value}\n")
            else:
                f.write("    {}\n")
            f.write("\n")

if __name__ == '__main__':
    # Specify the full paths to your input and output files
    devices_file = pathlib.Path('/Users/yuliia.maslovska/Downloads/devices.yaml')
    labs_file = pathlib.Path('/Users/yuliia.maslovska/Downloads/lab_envs.json')
    output_file = pathlib.Path('/Users/yuliia.maslovska/Downloads/device_with_lab4.yaml')

    # Call the merge_files function with the updated paths
    merge_files(devices_file, labs_file, output_file)
    print(f"Combined data written to '{output_file}'")
