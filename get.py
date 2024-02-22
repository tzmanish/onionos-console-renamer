# Import all the relevant libraries, try downloading them if missing
import json
import pandas as pd
from pathlib import Path

# Create empty lists to populate afterwards
EMU = Path('../')
output_file = Path('./data.csv')
data = []

# Loop through them
for f in EMU.iterdir():
    config_file = f/'config.json'
    if not (f.is_dir() and config_file.exists()):
        continue
    json_string = open(config_file, 'r')
    parsed = json.loads(json_string.read())
    data.append((f.name, parsed['label']))

    print(f"{f} \t> {parsed['label']}")

# Create Excel file
df = pd.DataFrame(data, columns=('Console_folder', 'Current_label'))
df.insert(2, 'New_label', '') 
print('\n\nCreating data file...')
df.to_csv(output_file, index=None)
print(output_file,'created')