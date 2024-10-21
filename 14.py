import json

def print_interface_status(data):
    # Print header
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 80)
    
    # Iterate over the data and print each row in the specified format
    for item in data['imdata']:
        attributes = item['l1PhysIf']['attributes']
        dn = attributes.get('dn', '')
        description = attributes.get('description', '')
        speed = attributes.get('speed', 'inherit')
        mtu = attributes.get('mtu', '')
        
        print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")

# Load JSON data from the file
with open('sample-data.json') as f:
    data = json.load(f)

# Call the function to print the output
print_interface_status(data)
