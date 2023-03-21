import os
import subprocess

os.system("rm -rf thirdweb/abi")
os.system("mkdir thirdweb/abi")

generated_abis = {}

directory = "node_modules/@thirdweb-dev/contracts-js/dist/abis"
output_path = "thirdweb/abi"

for filename in os.listdir(directory):
    try:
        path = os.path.join(directory, filename)
        output = subprocess.check_output(f"abi-gen --language Python -o {output_path} --abis {path}", shell=True).decode()
        generated_path = output.replace("\n", "").replace("\"", "").split("Created: ")[1]
        binding_path = generated_path.split("/")[2]
        os.system(f"mv {generated_path} {output_path}/{binding_path}.py")
        os.system(f"rm -rf {output_path}/{binding_path}")
        generated_abis[filename.replace(".json", "")] = binding_path
    except:
        print(f"Failed to generate binding for {filename}, continuing...")

for filename in os.listdir(output_path):
    path = os.path.join(output_path, filename)
    if os.path.isdir(path):
        os.system(f"rm -rf {path}")


for abi, binding in generated_abis.items():
    with open('thirdweb/abi/__init__.py', 'a') as file:
        file.write(f"\nfrom .{binding} import {abi} # pylint: disable=unused-import")