import json

# Load the JSON file
with open('sample-data.json') as f:
    data = json.load(f)

# Extract the interface data from the JSON file
interface_data = data['imdata']

# Print the table header
print('Interface Status')
print('=' * 80)
print('{:<50}{:<25}{:<10}{:<6}'.format('DN', 'Description', 'Speed', 'MTU'))
print('-' * 80)

# Print the interface data in tabular format
for interface in interface_data:
    dn = interface['fabricEthLan']['attributes']['dn']
    desc = interface['fabricEthLan']['attributes'].get('descr', '')
    speed = interface['fabricEthLan']['attributes'].get('speed', 'inherit')
    mtu = interface['fabricEthLan']['attributes'].get('mtu', '')
    print('{:<50}{:<25}{:<10}{:<6}'.format(dn, desc, speed, mtu))
