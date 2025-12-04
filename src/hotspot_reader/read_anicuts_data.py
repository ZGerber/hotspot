#!/usr/bin/env python3
"""
Read hotspot.data.aniCuts.txt and convert to CSV.

Reads the fixed-width format file, skips metadata header (first 44 lines),
and converts the data to a CSV file.
"""

import pandas as pd
import os
from pathlib import Path


def get_data_dir():
    """Get the data directory path, whether running as script or installed package."""
    # Get the package directory (where this file is located)
    package_dir = Path(__file__).parent
    
    # Look for data directory inside the package
    data_dir = package_dir / 'data'
    
    if data_dir.exists():
        return str(data_dir)
    
    # Fallback: try project root (for development)
    project_root = package_dir.parent
    data_dir = project_root / 'data'
    if data_dir.exists():
        return str(data_dir)
    
    # Last resort: current working directory
    return str(Path.cwd() / 'data')


def main():
    """Main function to read and convert the data file."""
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
    
    # Get data directory
    data_dir = get_data_dir()
    input_file = os.path.join(data_dir, 'hotspot.data.aniCuts.txt')
    output_file = os.path.join(data_dir, 'hotspot.data.aniCuts.csv')
    
    # Check if CSV file already exists
    if os.path.exists(output_file):
        print(f"CSV file already exists: {output_file}")
        print("Loading existing CSV file...")
        df = pd.read_csv(output_file)
        print(f"Loaded {len(df):,} rows from existing CSV file.")
    else:
        if not os.path.exists(input_file):
            print(f"Error: Input file not found: {input_file}")
            print("Please make sure the data file exists in the data directory.")
            return None
        
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
    
    return df


# Allow running as script with -i flag for interactive mode
if __name__ == "__main__":
    df = main()

