# Onion OS Console Renamer
A little script written in Python that allows you to rename as many consoles at once!
It was specifically written for [Onion OS](https://github.com/OnionUI).

## Usage
0. Backup your Emu folder!
1. Download the [zip file](https://github.com/tzmanish/onionos-console-renamer/archive/refs/heads/master.zip).
2. Extract the `onionos-console-renamer-master` folder in the Emu folder of your Onion OS.
3. Install [python3](https://www.python.org/downloads/) if you don't already have.
4. Install pandas using `pip install pandas` in your terminal.
5. If you want to use the default `data.csv` to sort consoles by release year, skip to step 9.
6. Run `python get.py` to generate `data.csv` with the console names.
7. Open `data.csv` from your working directory; in the New_label column, set the new names for the consoles.
8. Save and close the `data.csv` file.
9. Run the `python set.py` to update the console names!
