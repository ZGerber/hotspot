# Hotspot Data Reader

## What is this?

This software helps you work with cosmic ray data from the Telescope Array experiment.

## What does it do?

This program takes a text file with cosmic ray data and converts it into a CSV file. CSV files are easier to open in programs like Excel or Google Sheets, and they're easier to work with in Python.

## Installation

The easiest way to install this software is using pip. This will automatically install everything you need, including pandas.

1. Open a terminal (command prompt on Windows, Terminal on Mac/Linux)

2. Navigate to the hotspot folder:
   ```
   cd hotspot
   ```

3. Install the package:
   ```
   pip install .
   ```
   
   This will install the software and all its dependencies (including pandas).

## Requirements

If you prefer to install manually, you need:

- **Python 3** - (you probably already have this!)
- **pandas** - A Python library for working with data

To install pandas manually, type:
```
pip install pandas
```

## How to use it

### Option 1: Using the installed command (recommended)

After installing with `pip install .`, you can run the program from anywhere:

```
read-anicuts
```

### Option 2: Running as a Python module

You can also run it as a Python module:

```
python3 -m hotspot_reader.read_anicuts_data
```

(On some computers, you might use `python` instead of `python3`)

## Working with the data interactively

If you want to explore the data directly in Python after the script runs, you can use the `-i` option. This keeps Python running after the script finishes, so you can type commands and work with the data.

1. Run the program with the `-i` option:
   ```
   python3 -i -m hotspot_reader.read_anicuts_data
   ```
   

2. After the script finishes, Python will stay open and you'll see a `>>>` prompt. This means Python is waiting for you to type commands!

3. The data is stored in a variable called `df` (short for "dataframe"). You can use it to explore the data. Here are some examples you can try:

   - See the first few rows:
     ```
     df.head()
     ```
   
   - See how many rows and columns there are:
     ```
     df.shape
     ```
   
   - Look at a specific column (for example, the energy):
     ```
     df['Energy_EeV']
     ```
   
   - Find the highest energy cosmic ray:
     ```
     df['Energy_EeV'].max()
     ```
   
   - See basic statistics about the data:
     ```
     df.describe()
     ```

4. When you're done, type `exit()` or press Ctrl+D to close Python.

## What's in the data?

The CSV file contains information about cosmic ray events. Each row is one cosmic ray detection. The columns are:

- **Arrival_Year, Arrival_Month, Arrival_Day, Arrival_Hour, Arrival_Minute, Arrival_Second** - When the cosmic ray was detected
- **Zenith_angle_deg** - The angle from straight up (0° = straight up, 90° = horizon)
- **Energy_EeV** - How much energy the cosmic ray had (in EeV, which is a very large unit of energy)
- **RA_J2000** - Right Ascension, a coordinate that tells you where in the sky the cosmic ray came from (like longitude on Earth, but for the sky)
- **Dec_J2000** - Declination, another sky coordinate (like latitude on Earth, but for the sky)

## File locations

- **Input file**: `src/hotspot_reader/data/hotspot.data.aniCuts.txt` - This is the original data file (included in the package)
- **Output file**: `src/hotspot_reader/data/hotspot.data.aniCuts.csv` - This is the CSV file the program creates

The data files are included in the package, so they're available after installation. You can open the CSV file in Excel, Google Sheets, or any program that reads CSV files!

