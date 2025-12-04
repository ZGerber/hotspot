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

# Read the file, skipping the first 44 lines (metadata header)
file_path = os.path.join(project_root, 'data', 'hotspot.data.aniCuts.txt')
print(f"Reading data from {file_path}...")
print("Skipping first 44 lines (metadata header)...")

df = pd.read_csv(file_path,
                 skiprows=44,  # Skip metadata header
                 sep=r'\s+',   # Whitespace separator (handles multiple spaces)
                 header=None,  # No header row in data section
                 names=column_names)

print(f"\nDataFrame shape: {df.shape}")
print(f"\nColumn names:")
print(df.columns.tolist())
print(f"\nFirst few rows:")
print(df.head())
print(f"\nData types:")
print(df.dtypes)

# Write to CSV file
output_file = os.path.join(project_root, 'data', 'hotspot.data.aniCuts.csv')
print(f"\nWriting data to {output_file}...")
df.to_csv(output_file, index=False)
print(f"Successfully wrote {len(df):,} rows to {output_file}")

print("\n" + "="*80)
print("Conversion complete!")
print(f"Data loaded into DataFrame 'df' and saved to '{output_file}'")
print("="*80)

