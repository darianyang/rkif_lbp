import pandas as pd

# Load the CSV files
df1 = pd.read_csv('contacts_10i.csv')
df2 = pd.read_csv('holo_contacts_10i.csv')

# Get the column headers
headers1 = set(df1.columns)
headers2 = set(df2.columns)

# Compare the headers
if headers1 == headers2:
    print("The headers are the same.")
else:
    print("The headers are different.")
    #print("In file1 but not in file2:", headers1 - headers2)
    #print("In file2 but not in file1:", headers2 - headers1)

# Find shared columns
shared_cols = df1.columns.intersection(df2.columns)

# Subset both DataFrames to shared columns
df1_shared = df1[shared_cols]
df2_shared = df2[shared_cols]

# Concatenate the two DataFrames row-wise
merged_df = pd.concat([df1_shared, df2_shared], ignore_index=True)

# Write to a new CSV file
merged_df.to_csv('contacts_merged_10i.csv', index=False)
