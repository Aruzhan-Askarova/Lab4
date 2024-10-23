import json
import pandas as pd

# Load and parse the JSON data from the file
with open('sample-data.json') as f:
    data = json.load(f)

# Assuming the structure is a list of dictionaries
# and the keys to extract are 'dn', 'description', 'speed', 'mtu'
entries = []
for item in data['imdata']:
    dn = item['l1PhysIf']['attributes'].get('dn', '')
    description = item['l1PhysIf']['attributes'].get('descr', '')
    speed = item['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = item['l1PhysIf']['attributes'].get('mtu', '')
    
    entries.append([dn, description, speed, mtu])

# Create a DataFrame for better formatting
df = pd.DataFrame(entries, columns=['DN', 'Description', 'Speed', 'MTU'])

# Print the formatted output
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-" * 80)
for _, row in df.iterrows():
    print(f"{row['DN']:<50} {row['Description']:<20} {row['Speed']:<10} {row['MTU']:<6}")
