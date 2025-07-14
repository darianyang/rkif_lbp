#!/bin/bash

# Usage: ./downsample_csv.sh input.csv output.csv

input="$1"
output="$2"

# Check arguments
if [ $# -ne 2 ]; then
  echo "Usage: $0 input.csv output.csv"
  exit 1
fi

# Write header
head -n 1 "$input" > "$output"

# Write every 10th data row (skip header, then sample)
tail -n +2 "$input" | awk 'NR % 10 == 1' >> "$output"

echo "Downsampled CSV written to $output"

