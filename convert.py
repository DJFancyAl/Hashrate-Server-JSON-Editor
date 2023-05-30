# Imports
from os import listdir
import json
import shutil
import re

# Get Directory
print('Enter the directory containing the JSON files:')
# directory_name = input()
directory_name = r'''C:\Users\ablue\Desktop\Scripts\JSON Converter\Files'''
fileList = listdir(directory_name)

# Loop files
for file in fileList:
    # Get file name
    file_name = f"{directory_name}\{file}"
    old_filename = re.findall(r'(.*).json', file_name)

    # Copy file
    shutil.copyfile(file_name, old_filename[0] + '_old.json')

    # Open JSON File
    with open(file_name, "r") as f:
        data = json.load(f)

    # Change the description key
    print(f'Editing file: {file}')
    data['description'] = "234 Servers Mining Crypto"
    print('Step 1: ✅')
    # Remove seller_fee_basis_points
    data.pop('seller_fee_basis_points', None)
    print('Step 2: ✅')
    # Remove collecion
    data.pop('collection', None)
    print('Step 3: ✅')
    # Remove properties
    data['properties'].pop('creators', None)
    print('Step 4: ✅')
    print('------------')

    # Save file
    with open(file_name, "w") as new_file:
        json.dump(data, new_file, indent = 4)

    # Confirm
    print('File Changed!')
    print('------------')

print(f'{len(fileList)} FILES CHANGED!')