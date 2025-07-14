#!/bin/bash

# Usage: ./downsample_csv.sh input.csv output.csv

input="$1"
output="$2"

# Check arguments
if [ $# -ne 2 ]; then
  echo "Usage: $0 input.csv output.csv"
  exit 1
fi

# Write every 10th data row
awk 'NR % 10 == 1' "$input" > "$output"

echo "Downsampled CSV written to $output"

