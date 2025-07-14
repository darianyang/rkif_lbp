#!/bin/bash

# Usage: ./combine_csv.sh file1.csv file2.csv output.csv

file1="$1"
file2="$2"
output="$3"

# Check if all arguments are provided
if [ $# -ne 3 ]; then
  echo "Usage: $0 file1.csv file2.csv output.csv"
  exit 1
fi

# Combine the files
{
  head -n 1 "$file1"                # Write header from first file
  tail -n +2 "$file1"               # Write data from first file
  tail -n +2 "$file2"               # Write data from second file (skip header)
} > "$output"

echo "Combined CSV written to $output"

