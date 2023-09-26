import os
import pandas as pd
import glob


# Get a list of all the CSV files in the directory.
csv_files = glob.glob(r"E:\2ndYear\Slivia's project\mythalExp\batch1\mValues/*.csv")
# Create an empty list to store the data frames.
data_frames = []
# Iterate over the list of CSV files and read each file into a data frame, renaming the first column.
for filename in csv_files:
    df = pd.read_csv(filename, low_memory=False)
    # Set the `id` column as the index.
    df = df.set_index('Unnamed: 0')
    df = df.rename_axis('id', axis=0)
    data_frames.append(df)
    

comb=data_frames[0].join(data_frames[1:])

comb.to_csv(r"E:\2ndYear\Slivia's project\mythalExp\batch1\mValues\3_combined_mval.csv")
