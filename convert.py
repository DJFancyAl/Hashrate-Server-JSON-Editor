# Imports
import json
import shutil
import re

# Get Filename
print('Enter the filename (with .json file extension):')
filename = input()

old_filename = re.findall(r'(.*).json', filename)
print(old_filename[0])

# Copy file
shutil.copyfile(filename, old_filename[0] + '_old.json')

# Open JSON File
with open(filename, "r") as f:
    data = json.load(f)

# Change the description key
data['description'] = "234 Servers Mining Crypto"
print('Step 1: ✅')
data.pop('seller_fee_basis_points', None)
print('Step 2: ✅')
data.pop('collection', None)
print('Step 3: ✅')
data['properties'].pop('creators', None)
print('Step 4: ✅')

# Save file
with open(filename, "w") as file:
    json.dump(data, file, indent = 4)

# Confirm
print('File Changed!')