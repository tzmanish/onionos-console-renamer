# Import all the relevant libraries, try downloading them if missing
import pandas as pd
import json
from pathlib import Path

EMU=Path('../')
input_file = Path('./data.csv')

# Read data.xlsx if it exists
if not input_file.exists():
    raise FileNotFoundError(f'{input_file} not found!')

print(f'{input_file} found!')
print('Proceeding...')
df = pd.read_csv(input_file, dtype=str)
print('Excluding blank entries...')
df = df[df['New_label'].notna()] # Get rid of empty values, the ones we are not going to update

# Let's make sure there are actual entries to update, otherwise let's not waste time
if df.empty:
    raise('No entries to update...')

print(f'Entries to update: {len(df)}')

# The core loop to read and replace current (old) values with new ones
for n in df[['Console_folder', 'Current_label', 'New_label']].to_dict('records'):
    print(f"\t- {n['Current_label']}", end=' \t: ')
    config_file = EMU/n['Console_folder']/'config.json'

    if not config_file.exists():
        print(f'{config_file} not found. skipping...')
        continue

    print(f"{n['New_label']}")
    with open(config_file) as f:
        data = json.load(f)

    data['label'] = n['New_label']
    
    with open(config_file, 'w') as f:
        json.dump(data, f, indent=2)
