#!/usr/bin/env python3
"""
Read hotspot.data.aniCuts.txt and convert to CSV.

Reads the fixed-width format file, skips metadata header (first 44 lines),
and converts the data to a CSV file.
"""

import pandas as pd
import os

# Get the project root directory (parent of scripts directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Define column names based on the file format description
column_names = [
    'Arrival_Year',
    'Arrival_Month',
    'Arrival_Day',
    'Arrival_Hour',
    'Arrival_Minute',
    'Arrival_Second',
    'Zenith_angle_deg',
    'Energy_EeV',
    'RA_J2000',
    'Dec_J2000'
]

# Define input and output file paths
input_file = os.path.join(project_root, 'data', 'hotspot.data.aniCuts.txt')
output_file = os.path.join(project_root, 'data', 'hotspot.data.aniCuts.csv')

# Check if CSV file already exists
if os.path.exists(output_file):
    print(f"CSV file already exists: {output_file}")
    print("Loading existing CSV file...")
    df = pd.read_csv(output_file)
    print(f"Loaded {len(df):,} rows from existing CSV file.")
else:
    # Read the file, skipping the first 44 lines (metadata header)
    print(f"Reading data from {input_file}...")
    print("Skipping first 44 lines (metadata header)...")
    
    df = pd.read_csv(input_file,
                     skiprows=44,  # Skip metadata header
                     sep=r'\s+',   # Whitespace separator (handles multiple spaces)
                     header=None,  # No header row in data section
                     names=column_names)
    
    # Write to CSV file
    print(f"\nWriting data to {output_file}...")
    df.to_csv(output_file, index=False)
    print(f"Successfully wrote {len(df):,} rows to {output_file}")

print(f"\nDataFrame shape: {df.shape}")
print(f"\nColumn names:")
print(df.columns.tolist())
print(f"\nFirst few rows:")
print(df.head())
print(f"\nData types:")
print(df.dtypes)

print("\n" + "="*80)
print("Data loaded into DataFrame 'df'")
print("="*80)

